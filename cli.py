import inquirer
type_list = [
  inquirer.List('game',
                message="A cosa stai nerdando ? ",
                choices=['Savage', 'CoC', 'Vampire', '1572', 'Simple'],
            ),
]
