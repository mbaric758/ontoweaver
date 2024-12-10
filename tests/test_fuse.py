import logging

from docs import ontoweaver


def test_fuse():
    nodes = [
        ("Source:1", "Source", {"p1":"z"}),
        ("Source:1", "Source", {"p2":"y"}), # Simple duplicate.
        ("Target:2", "Target", {}),
        ("Target:2", "Target1", {"p1":"x", "p2":"y"}),
        ("Target:2", "Target2", {"p2":"z"}),
    ]

    on_ID = ontoweaver.serialize.ID()
    congregater = docs.ontoweaver.congregate.Nodes(on_ID)
    congregater(nodes)

    as_keys  = docs.ontoweaver.merge.string.UseKey()
    as_first = docs.ontoweaver.merge.string.UseFirst()
    in_lists = docs.ontoweaver.merge.dictry.Append()
    fuser = docs.ontoweaver.fuse.Members(docs.ontoweaver.base.Node,
                                         merge_ID    = as_keys,
                                         merge_label = as_first,
                                         merge_prop  = in_lists,
                                         )

    fusioner = ontoweaver.fusion.Reduce(fuser)
    fusioned = fusioner(congregater)

    logging.debug("Fusioned items:")
    for f in fusioned:
        logging.debug("  "+repr(f))

    assert(len(fusioned) == 2)
    for e in fusioned:
        assert("p1" in e.properties)
        assert("p2" in e.properties)
        assert("y" in e.properties["p2"])

    assert(len(fuser.ID_mapping) == 0) # Only self-mappings.

    as_sets = docs.ontoweaver.merge.string.OrderedSet(".")
    in_lists2 = docs.ontoweaver.merge.dictry.Append(";")
    fuser2 = docs.ontoweaver.fuse.Members(docs.ontoweaver.base.Node,
                                          merge_ID    = as_keys,
                                          merge_label = as_sets,
                                          merge_prop  = in_lists2,
                                          )

    fusioner2 = ontoweaver.fusion.Reduce(fuser2)
    fusioned2 = fusioner2(congregater)

    logging.debug("Fusioned items:")
    for f in fusioned2:
        logging.debug("  "+repr(f))

    assert(len(fusioned2) == 2)
    for e in fusioned2:
        assert("p1" in e.properties)
        assert("p2" in e.properties)
        assert("y" in e.properties["p2"])


if __name__ == "__main__":
    test_fuse()
