<h1 align="center">ACP Macro Preprocessor</h1>
<p align="center">
    A custom designed macro preprocessor supporting macro with same syntax across nasm, cpp and python programmes</p>


## Features
The Macro preprocessor supports :
1. Single-line macro
2. Multi-line macro
3. Nested macro
4. Comment lines (for all the given three languages)
5. Un-defining and Re-defining of macro
6. Conditional macro
7. As many numbers of parameters and variables.
8. As many levels of nesting.
9. Less or more number of parameters than defined in the macro. If given a lesser number of parameters than defined, there must be “,” as separator for no parameters. If given more number of parameters than defined, it will accept the first 'n' number of arguments, where 'n' is the defined no of parameters.


## Macro Definition

1. Single-line Macro : 
    ```
    @MACRO<space>[name]<space>:
    ```
2. Multi-line Macro : 
    ```
    @MACRO<space>[name]<space>:-[{…}]
    ```
3. Un-defining Macro :
    ```
	%undef $[label]
    ```
4. Re-defining Macro :
    ```
	%redef $[label]
    ```
5. Conditional Macro :
    ```
	%ifdef $[label] 
	%ifndef $[label]
    ```

    \* [label] is the ordered number of defined macros.


## 🛠 Installation & Set Up

1. Setup Python3 on System

2. Download or clone the project

3. Install Colorama.

    ```
    $ pip install colorama
    ```

4. Run the acpmac.py file adding the name of the file to be processed as a parameter. Make sure the file to be processed is in the same directory as of acpmac.py.

    ```
    $ python3 acpmac.py <file_name>
    ```

5. The output will be a preprocessed file which will be displayed on the terminal