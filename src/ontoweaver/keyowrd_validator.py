import inspect
import logging
from . import errormanager
from . import transformer
from rapidfuzz import process
import yaml

logger = logging.getLogger("ontoweaver")

class KeywordResolver(errormanager.ErrorManager):
    """Class used for resolving keyword issues in the YAML file."""

    def allow_keywords(self, new_keywords: list):
        """Add new keywords to the resolver."""

        if new_keywords:
            self.allowed_keywords.update(new_keywords)

    def __init__(self, raise_errors: bool = True, allow_keywords: list = None):
        self.raise_errors = raise_errors

        self.allowed_keywords = set()

        # Allow some defaults such as transformers.
        # FIXME: This should also include the keywords specific to transformers, but filtering so that they are valid only for the correct transformer.
        self.allowed_keywords.update(name for name, obj in inspect.getmembers(transformer, inspect.isclass))

        self.allow_keywords(allow_keywords)

        print(self.allowed_keywords)
        super().__init__(self.raise_errors)


    # The minimum score for a match to be considered valid. Check if 70 is appropriate.
    def _resolve_one(self, word: str, min_score: int = 70):
        """Resolve a single word. Suggest closest match if not correct."""
        if word in self.allowed_keywords:
            return word

        match = process.extractOne(word, self.allowed_keywords, score_cutoff=min_score)
        if match:
            closest_alt, score, _ = match
            logger.error(f"Invalid keyword '{word}'. Did you mean '{closest_alt}'?") #FIXME: Should raise logger error, but how to solve transformer specific keywords?
            return closest_alt
        else:
            logger.error(f"Invalid keyword '{word}'. No close matches found.") #FIXME: Should raise logger error, but how to solve transformer specific keywords?

    def _resolve_yaml(self, data, min_score: int = 70, in_match: bool = False):
        """Recursively validate keys in nested dict extracted from YAML.
        Keys are validated everywhere except immediate dict keys inside a `match` list, because those are user-defined values to match against.
        """

        if isinstance(data, dict):
            # Recursively store the resulting dict in this structure, with the idea of then returning this to the user
            # as a suggested corrected version of their input.
            self.resolved = {}
            for key, value in data.items():
                # If we're inside a match list, skip validation for the first-level keys.
                if in_match:
                    resolved_key = key
                else:
                    resolved_key = self._resolve_one(key, min_score) or key

                # If this key is 'match', recurse with in_match=True
                if resolved_key == "match" and isinstance(value, list):
                    self.resolved[resolved_key] = self._resolve_yaml(value, min_score, in_match=True)
                else:
                    # Recurse normally — after skipping, we reset in_match=False.
                    if isinstance(value, (dict, list)):
                        self.resolved[resolved_key] = self._resolve_yaml(value, min_score, in_match=False)
                    else:
                        self.resolved[resolved_key] = value
            # FIXME: Should not return resolved like this, but as logging? Or separate function.

        elif isinstance(data, list):
            return [self._resolve_yaml(item, min_score, in_match=in_match) for item in data]

    def __call__(self, yaml_dict, min_score: int = 70):

        if isinstance(yaml_dict, str):
            self._resolve_one(yaml_dict, min_score)

        if isinstance(yaml_dict, (dict, list)):
            self._resolve_yaml(yaml_dict, min_score)

        try:
            {w: self._resolve_one(w, min_score) for w in yaml_dict}
        except TypeError:
            raise logger.error("String, iterable of strings, dict, or list")


    def write_suggested_yaml(self):

        print(yaml.dump(self.resolved, sort_keys=False))
