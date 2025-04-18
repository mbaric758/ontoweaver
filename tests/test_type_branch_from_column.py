def test_match_type_from_column():
    from . import testing_functions
    import logging
    import ontoweaver

    logging.basicConfig(level=logging.DEBUG)

    directory_name = "match_type_from_column"

    assert_nodes = [('fridge:kitchen_furniture', 'kitchen_furniture', {'localisation': 'Marykitchen', 'blabla': 'blabla', 'source_columns': 'furniture'}),
                    ('Peter:person', 'person', {'blabla': 'blabla', 'source_columns': 'name'}),
                    ('sofa:rest_of_house_furniture', 'rest_of_house_furniture', {'localisation': 'Paulbathroom', 'blabla': 'blabla', 'source_columns': 'furniture'}),
                    ('chair:kitchen_furniture', 'kitchen_furniture', {'localisation': 'Peterkitchen', 'blabla': 'blabla', 'source_columns': 'furniture'}),
                    ('Paul:person', 'person', {'blabla': 'blabla', 'source_columns': 'name'}),
                    ('Mary:person', 'person', {'blabla': 'blabla', 'source_columns': 'name'}),
                    ]

    assert_edges = [('', 'sofa:rest_of_house_furniture', 'Paul:person', 'will_sit', {'blabla': 'blabla'}),
                    ('', 'chair:kitchen_furniture', 'Peter:person', 'will_not_sit', {'blabla': 'blabla'}),
                    ('', 'fridge:kitchen_furniture', 'Mary:person', 'will_not_sit', {'blabla': 'blabla'}),
                    ]

    data_mapping = {f"tests/{directory_name}/data.csv": f"tests/{directory_name}/mapping.yaml"}

    nodes, edges = ontoweaver.extract(filename_to_mapping=data_mapping, affix="suffix")

    fnodes, fedges = ontoweaver.fusion.reconciliate(nodes, edges, separator=",")

    assert_node_set = testing_functions.convert_to_set(assert_nodes)
    f_node_set = testing_functions.convert_to_set(fnodes)

    assert assert_node_set == f_node_set, "Nodes are not equal."

    assert_edge_set = testing_functions.convert_to_set(assert_edges)
    f_edge_set = testing_functions.convert_to_set(fedges)

    assert assert_edge_set == f_edge_set, "Edges are not equal."


if __name__ == "__main__":
    test_match_type_from_column()