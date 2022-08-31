FILE_DATA = """Smith, Joan -- ut
    Voluptatem ipsam et at.
O'Shea, Peter -- non
    Facere et necessitatibus animi.
McLaughlin, Mariah -- consequatur
    Eveniet temporibus ducimus amet eaque.
Lang, Agustina -- pariatur
    Unde voluptas sit fugit.
Bradtke, Nikko -- et
    Maiores ab officia sed.
Adams, Luis -- error
    Repellendus alias officia amet et perspiciatis.
Lehner, Matilde -- nesciunt
    Incidunt et ut necessitatibus porro.
Ortiz, Anita -- fuga
    Tempore eos et hic.
Koch, Berry -- vel
    Laborum perferendis inventore eveniet.
Cartwright, Nicolas -- et
    Optio aliquid earum exercitationem vitae fugit.
"""  # mock filename to be processed
ITEMS_EX = [{"other": "Unit", "name": "Test", "full_name": "Unit, Test"}]
LIST_DICT_DATA = [{'last_name': 'Graham', 'name': 'Mckenna', 'full_name': 'Graham, Mckenna'},
{'last_name': 'Marvin', 'name': 'Garfield', 'full_name': 'Marvin, Garfield'},
{'last_name': 'McLaughlin', 'name': 'Mariah', 'full_name': 'McLaughlin, Mariah'},
{'last_name': 'Lang', 'name': 'Agustina', 'full_name': 'Lang, Agustina'},
{'last_name': 'Bradtke', 'name': 'Nikko', 'full_name': 'Bradtke, Nikko'},
{'last_name': 'Adams', 'name': 'Luis', 'full_name': 'Adams, Luis'},
{'last_name': 'Lehner', 'name': 'Matilde', 'full_name': 'Lehner, Matilde'},
{'last_name': 'Ortiz', 'name': 'Anita', 'full_name': 'Ortiz, Anita'},
{'last_name': 'Koch', 'name': 'Berry', 'full_name': 'Koch, Berry'},
{'last_name': 'Cartwright', 'name': 'Nicolas', 'full_name': 'Cartwright, Nicolas'},
{'last_name': 'Fisher', 'name': 'Elmo', 'full_name': 'Fisher, Elmo'},
{'last_name': 'Kunze', 'name': 'Gertrude', 'full_name': 'Kunze, Gertrude'},
{'last_name': 'Stanton', 'name': 'Davin', 'full_name': 'Stanton, Davin'},
{'last_name': 'Runolfsdottir', 'name': 'Roy', 'full_name': 'Runolfsdottir, Roy'},
{'last_name': 'Rogahn', 'name': 'Colby', 'full_name': 'Rogahn, Colby'},
{'last_name': 'Tromp', 'name': 'Ryley', 'full_name': 'Tromp, Ryley'},
{'last_name': 'Hoppe', 'name': 'Stanley', 'full_name': 'Hoppe, Stanley'},
{'last_name': 'Shanahan', 'name': 'Bethel', 'full_name': 'Shanahan, Bethel'},
{'last_name': 'Hills', 'name': 'Samanta', 'full_name': 'Hills, Samanta'},
{'last_name': 'McGlynn', 'name': 'Thad', 'full_name': 'McGlynn, Thad'},
{'last_name': 'McGlynn', 'name': 'Katrina', 'full_name': 'McGlynn, Katrina'},
{'last_name': 'Lynch', 'name': 'Norma', 'full_name': 'Lynch, Norma'},
{'last_name': 'Bahringer', 'name': 'Lennie', 'full_name': 'Bahringer, Lennie'},
{'last_name': 'Tillman', 'name': 'Madison', 'full_name': 'Tillman, Madison'},
{'last_name': 'Stoltenberg', 'name': 'Donna', 'full_name': 'Stoltenberg, Donna'}]

LIST_DICT_DATA_IRREGULAR = [{'last_name': 'Graham', 'name': 'Mckenna', 'full_name': 'Graham, Mckenna'},
{'last_name': 'Graham', 'name': 'Mckenna', 'full_name': 'Graham, Mckenna'},
{'last_name': 'Graham', 'name': 'Mckenna', 'full_name': 'Graham, Mckenna'},
{'last_name': 'Graham', 'name': 'Mckenna', 'full_name': 'Graham, Mckenna'},
{'last_name': 'Graham', 'name': 'Mckenna', 'full_name': 'Graham, Mckenna'},
{'last_name': 'Graham', 'name': 'Mckenna', 'full_name': 'Graham, Mckenna'},
{'last_name': 'Graham', 'name': 'Mckenna', 'full_name': 'Graham, Mckenna'},
{'last_name': 'Marvin', 'name': 'Garfield', 'full_name': 'Marvin, Garfield'}]