import logging
from . import errormanager
from rapidfuzz import process

logger = logging.getLogger("ontoweaver")

class KeywordResolver(errormanager.ErrorManager):
    """Class used for resolving keyword issues in the YAML file."""

    def allow_keywords(self, new_keywords: list):
        """Add new keywords to the resolver."""
        self.allowed_keywords.extend(new_keywords)
        self.all_keywords = list(set(self.allowed_keywords))  # avoid duplicates

    def __init__(self, allowed_keywords: list = None):
        self.raise_errors = True

        # Allow some defaults such as transformers.
        # FIXME: This should also include the keywords specific to transformers, but filtering so that they are valid only for the correct transformer.
        self.allowed_keywords = [
            "rowIndex", "split", "cat", "map", "cat_format",
            "translate", "string", "replace"
        ]

        # Append new keywords if provided. Should be specific to the use case (target / subject parsing, etc.)
        self.allow_keywords(allowed_keywords)
        self.all_keywords = list(self.allowed_keywords)
        super().__init__(self.raise_errors)


    # The minimum score for a match to be considered valid. Check if 70 is appropriate.
    def _resolve_one(self, word: str, min_score: int = 70):
        """Resolve a single word. Suggest closest match if not correct."""
        if word in self.allowed_keywords:
            return word

        match = process.extractOne(word, self.all_keywords, score_cutoff=min_score)
        if match:
            closest_alt, score, _ = match
            logger.error(f"Invalid keyword '{word}'. Did you mean '{closest_alt}'?")
        else:
            logger.error(f"Invalid keyword '{word}'. No close matches found.")
        return None

    def _resolve_yaml(self, data, min_score: int = 70, in_match: bool = False):
        """Recursively validate keys in nested dict extracted from YAML.
        Keys are validated everywhere except immediate dict keys inside a `match` list, because those are user-defined values to match against.
        """

        if isinstance(data, dict):
            # Recursively store the resulting dict in this structure, with the idea of then returning this to the user
            # as a suggested corrected version of their input.
            resolved = {}
            for key, value in data.items():
                # If we're inside a match list, skip validation for the first-level keys.
                if in_match:
                    resolved_key = key
                else:
                    resolved_key = self._resolve_one(key, min_score) or key

                # If this key is 'match', recurse with in_match=True
                if resolved_key == "match" and isinstance(value, list):
                    resolved[resolved_key] = self._resolve_yaml(value, min_score, in_match=True)
                else:
                    # Recurse normally — after skipping, we reset in_match=False.
                    if isinstance(value, (dict, list)):
                        resolved[resolved_key] = self._resolve_yaml(value, min_score, in_match=False)
                    else:
                        resolved[resolved_key] = value
            # FIXME: Should not return resolved like this, but as logging? Or separate function.
            return resolved

        elif isinstance(data, list):
            return [self._resolve_yaml(item, min_score, in_match=in_match) for item in data]

        else:
            return data # FIXME: Possibly should be true / false?

    def __call__(self, words, min_score: int = 70):

        if isinstance(words, str):
            return self._resolve_one(words, min_score)

        if isinstance(words, (dict, list)):
            return self._resolve_yaml(words, min_score)

        try:
            return {w: self._resolve_one(w, min_score) for w in words}
        except TypeError:
            raise ValueError("resolve() expected a string, iterable of strings, dict, or list")
