grammar_rules = {
    "primary_expression": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET primary_expression", "'(' expression ')'"],
    "postfix_expression": ["primary_expression", "postfix_expression '[' expression ']'", "postfix_expression '(' ')'",
                           "postfix_expression '(' argument_expression_list ')'", "postfix_expression '.' IDENTIFIER",
                           "postfix_expression PTR_OP IDENTIFIER", "postfix_expression INC_OP", "postfix_expression DEC_OP"],
    "argument_expression_list": ["assignment_expression", "argument_expression_list ',' assignment_expression"],
    "unary_expression": ["postfix_expression", "INC_OP unary_expression", "DEC_OP unary_expression",
                         "unary_operator cast_expression", "SIZEOF unary_expression",
                         "SIZEOF '(' type_name ')'"],
    "unary_operator": ["'&'", "'*'", "'+'", "'-'", "'~'", "'!'"],
    "cast_expression": ["unary_expression", "'(' type_name ')' cast_expression"],
    "multiplicative_expression": ["cast_expression", "multiplicative_expression '*' cast_expression",
                                   "multiplicative_expression '/' cast_expression",
                                   "multiplicative_expression '%' cast_expression"],
    "additive_expression": ["multiplicative_expression", "additive_expression '+' multiplicative_expression",
                             "additive_expression '-' multiplicative_expression"],
    "shift_expression": ["additive_expression", "shift_expression LEFT_OP additive_expression",
                          "shift_expression RIGHT_OP additive_expression"],
    "relational_expression": ["shift_expression", "relational_expression '<' shift_expression",
                               "relational_expression '>' shift_expression",
                               "relational_expression LE_OP shift_expression",
                               "relational_expression GE_OP shift_expression"],
    "equality_expression": ["relational_expression", "equality_expression EQ_OP relational_expression",
                             "equality_expression NE_OP relational_expression"],
    "and_expression": ["equality_expression", "and_expression '&' equality_expression"],
    "exclusive_or_expression": ["and_expression", "exclusive_or_expression '^' and_expression"],
    "inclusive_or_expression": ["exclusive_or_expression", "inclusive_or_expression '|' exclusive_or_expression"],
    "logical_and_expression": ["inclusive_or_expression", "logical_and_expression AND_OP inclusive_or_expression"],
    "logical_or_expression": ["logical_and_expression", "logical_or_expression OR_OP logical_and_expression"],
    "conditional_expression": ["logical_or_expression", "logical_or_expression '?' expression ':' conditional_expression"],
    "assignment_expression": ["conditional_expression", "unary_expression assignment_operator assignment_expression"],
    "assignment_operator": ["'='", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN",
                             "LEFT_ASSIGN", "RIGHT_ASSIGN", "AND_ASSIGN", "XOR_ASSIGN", "OR_ASSIGN"],
    "expression": ["assignment_expression", "expression ',' assignment_expression"],
    "constant_expression": ["conditional_expression"],
    "declaration": ["declaration_specifiers ';'", "declaration_specifiers init_declarator_list ';'"],
    "declaration_specifiers": ["storage_class_specifier", "type_specifier", "type_qualifier"],
    "init_declarator_list": ["init_declarator", "init_declarator_list ',' init_declarator"],
    "init_declarator": ["declarator", "declarator '=' initializer"],
    "storage_class_specifier": ["TYPEDEF", "EXTERN", "STATIC", "AUTO", "REGISTER"],
    "type_specifier": ["VOID", "CHAR", "SHORT", "INT", "LONG", "FLOAT", "DOUBLE", "SIGNED", "UNSIGNED",
                        "struct_or_union_specifier", "enum_specifier", "TYPE_NAME"],
    "struct_or_union_specifier": ["struct_or_union IDENTIFIER '{' struct_declaration_list '}'",
                                    "struct_or_union '{' struct_declaration_list '}'",
                                    "struct_or_union IDENTIFIER"],
    "struct_or_union": ["STRUCT", "UNION"],
    "struct_declaration_list": ["struct_declaration", "struct_declaration_list struct_declaration"],
    "struct_declaration": ["specifier_qualifier_list struct_declarator_list ';'"],
    "specifier_qualifier_list": ["type_specifier", "type_qualifier", "type_specifier specifier_qualifier_list",
                                  "type_qualifier specifier_qualifier_list"],
    "struct_declarator_list": ["struct_declarator", "struct_declarator_list ',' struct_declarator"],
    "struct_declarator": ["declarator", "':' constant_expression", "declarator ':' constant_expression"],
    "enum_specifier": ["ENUM '{' enumerator_list '}'", "ENUM IDENTIFIER '{' enumerator_list '}'",
                        "ENUM IDENTIFIER"],
    "enumerator_list": ["enumerator", "enumerator_list ',' enumerator"],
    "enumerator": ["IDENTIFIER", "IDENTIFIER '=' constant_expression"],
    "type_qualifier": ["CONST", "VOLATILE"],
    "declarator": ["pointer direct_declarator", "direct_declarator"],
    "direct_declarator": ["IDENTIFIER", "'(' declarator ')'", "direct_declarator '[' constant_expression ']'",
                            "direct_declarator '[' ']'", "direct_declarator '(' parameter_type_list ')'",
                            "direct_declarator '(' identifier_list ')'", "direct_declarator '(' ')'",],
    "pointer": ["''", "'' type_qualifier_list", "'' pointer", "'' type_qualifier_list pointer"],
    "type_qualifier_list": ["type_qualifier", "type_qualifier_list type_qualifier"],
    "parameter_type_list": ["parameter_list", "parameter_list ',' ELLIPSIS"],
    "parameter_list": ["parameter_declaration", "parameter_list ',' parameter_declaration"],
    "parameter_declaration": ["declaration_specifiers declarator", "declaration_specifiers",
                                "declaration_specifiers abstract_declarator"],
    "identifier_list": ["IDENTIFIER", "identifier_list ',' IDENTIFIER"],
    "type_name": ["specifier_qualifier_list", "specifier_qualifier_list abstract_declarator"],
    "abstract_declarator": ["pointer", "direct_abstract_declarator", "pointer direct_abstract_declarator"],
    "direct_abstract_declarator": ["'(' abstract_declarator ')'", "'[' ']'", "'[' constant_expression ']'",
                                      "direct_abstract_declarator '[' ']'",
                                      "direct_abstract_declarator '[' constant_expression ']'",
                                      "'(' ')'", "'(' parameter_type_list ')'",
                                      "direct_abstract_declarator '(' ')'",
                                      "direct_abstract_declarator '(' parameter_type_list ')'"],
    "initializer": ["assignment_expression", "'{' initializer_list '}'", "'{' initializer_list ',' '}'"],
    "initializer_list": ["initializer", "initializer_list ',' initializer"],
    "statement": ["labeled_statement", "compound_statement", "expression_statement", "selection_statement",
                    "iteration_statement", "jump_statement"],
    "labeled_statement": ["IDENTIFIER ':' statement", "CASE constant_expression ':' statement", "DEFAULT ':' statement"],
    "compound_statement": ["'{' '}'", "'{' statement_list '}'", "'{' declaration_list '}'", "'{' declaration_list statement_list '}'"],
    "declaration_list": ["declaration", "declaration_list declaration"],
    "statement_list": ["statement", "statement_list statement"],
    "expression_statement": ["';'", "expression ';'"],
    "selection_statement": ["IF '(' expression ')' statement", "IF '(' expression ')' statement ELSE statement",
                              "SWITCH '(' expression ')' statement"],
    "iteration_statement": ["WHILE '(' expression ')' statement", "DO statement WHILE '(' expression ')' ';'",
                              "FOR '(' expression_statement expression_statement ')' statement",
                              "FOR '(' expression_statement expression_statement expression ')' statement"],
    "jump_statement": ["GOTO IDENTIFIER ';'", "CONTINUE ';'", "BREAK ';'", "RETURN ';'", "RETURN expression ';'"],
    "translation_unit": ["external_declaration", "translation_unit external_declaration"],
    "external_declaration": ["function_definition", "declaration"],
    "function_definition": ["declaration_specifiers declarator declaration_list compound_statement",
                              "declaration_specifiers declarator compound_statement",
                              "declarator declaration_list compound_statement",
                              "declarator compound_statement"]
                  
}

# Terminal symbols
terminals = set([
    "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "PTR_OP", "INC_OP", "DEC_OP", "LEFT_OP", "RIGHT_OP",
    "LE_OP", "GE_OP", "EQ_OP", "NE_OP", "AND_OP", "OR_OP", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "ADD_ASSIGN",
    "SUB_ASSIGN", "LEFT_ASSIGN", "RIGHT_ASSIGN", "AND_ASSIGN", "XOR_ASSIGN", "OR_ASSIGN", "TYPEDEF", "EXTERN",
    "STATIC", "AUTO", "REGISTER", "VOID", "CHAR", "SHORT", "INT", "LONG", "FLOAT", "DOUBLE", "SIGNED", "UNSIGNED",
    "STRUCT", "UNION", "ENUM", "ELLIPSIS", "CASE", "DEFAULT", "IF", "ELSE", "SWITCH", "WHILE", "DO", "FOR", "GOTO",
    "CONTINUE", "BREAK", "RETURN", "TYPE_NAME", "EOF", "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", "'->'",
    "'++'", "'--'", "'&'", "'*'", "'+'", "'-'", "'~'", "'!'", "'/'", "'%'", "'<<'", "'>>'", "'<'", "'>'", "'<='",
    "'>='", "'=='", "'!='", "'^'", "'|'", "'&&'", "'||'", "'?'", "':'", "';'", "','", "'='",
])

# Non-terminal symbols
non_terminals = set(grammar_rules.keys())

# Follow sets for each non-terminal
follow_sets = {
    "primary_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('"],
    "postfix_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('"],
    "argument_expression_list": ["')'"],
    "unary_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                          "+", "-", "~", "!"],
    "unary_operator": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                       "+", "-", "~", "!"],
    "cast_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                        "+", "-", "~", "!"],
    "multiplicative_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&",
                                   "*", "+", "-", "~", "!"],
    "additive_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&",
                             "*", "+", "-", "~", "!"],
    "shift_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&",
                           "*", "+", "-", "~", "!"],
    "relational_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&",
                                 "*", "+", "-", "~", "!"],
    "equality_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&",
                               "*", "+", "-", "~", "!"],
    "and_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*", "+",
                        "-", "~", "!"],
    "exclusive_or_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&",
                                   "*", "+", "-", "~", "!"],
    "inclusive_or_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&",
                                   "*", "+", "-", "~", "!"],
    "logical_and_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                                  "+", "-", "~", "!"],
    "logical_or_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                                 "+", "-", "~", "!"],
    "conditional_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                                  "+", "-", "~", "!"],
    "assignment_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                                 "+", "-", "~", "!"],
    "expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                      "+", "-", "~", "!"],
    "constant_expression": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                               "+", "-", "~", "!"],
    "declaration": ["'", "'", "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                       "+", "-", "~", "!"],
    "declaration_specifiers": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                                 "+", "-", "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char",
                                 "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union", "enum",
                                 "EOF"],
    "init_declarator_list": ["';'"],
    "init_declarator": ["',', ';'"],
    "storage_class_specifier": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                                  "+", "-", "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char",
                                  "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union",
                                  "enum", "EOF"],
    "type_specifier": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                          "+", "-", "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char", "short",
                          "int", "long", "float", "double", "signed", "unsigned", "struct", "union", "enum", "EOF"],
    "struct_or_union_specifier": ["IDENTIFIER", "'{'", "typedef", "extern", "static", "auto", "register", "void", "char",
                                     "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union",
                                     "enum", "EOF"],
    "struct_or_union": ["IDENTIFIER", "'{'", "typedef", "extern", "static", "auto", "register", "void", "char", "short",
                           "int", "long", "float", "double", "signed", "unsigned", "struct", "union", "enum", "EOF"],
    "struct_declaration_list": ["IDENTIFIER", "'{'", "typedef", "extern", "static", "auto", "register", "void", "char",
                                   "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union",
                                   "enum", "EOF"],
    "struct_declaration": ["';'"],
    "specifier_qualifier_list": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                                    "+", "-", "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char",
                                    "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union",
                                    "enum", "EOF"],
    "struct_declarator_list": ["';'"],
    "struct_declarator": ["','", "';'"],
    "enum_specifier": ["IDENTIFIER", "'{'", "typedef", "extern", "static", "auto", "register", "void", "char", "short",
                          "int", "long", "float", "double", "signed", "unsigned", "struct", "union", "enum", "EOF"],
    "enumerator_list": ["'}'"],
    "enumerator": ["','", "'}'"],
    "type_qualifier": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                          "+", "-", "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char",
                          "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union",
                          "enum", "EOF"],
    "declarator": ["';'"],
    "direct_declarator": ["';'"],
    "pointer": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*", "+", "-",
                       "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char", "short", "int",
                       "long", "float", "double", "signed", "unsigned", "struct", "union", "enum", "EOF"],
    "type_qualifier_list": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                               "+", "-", "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char",
                               "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union",
                               "enum", "EOF"],
    "parameter_type_list": ["')'"],
    "parameter_list": ["','", ")"],
    "parameter_declaration": ["','", ")"],
    "identifier_list": ["','"],
    "type_name": ["';'"],
    "abstract_declarator": ["';'"],
    "direct_abstract_declarator": ["';'"],
    "initializer": ["',', '}'"],
    "initializer_list": ["'}'"],
    "statement": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*", "+", "-",
                     "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char", "short", "int",
                     "long", "float", "double", "signed", "unsigned", "struct", "union", "enum", "EOF", "case",
                     "default", "if", "switch", "while", "do", "for", "goto", "continue", "break", "return"],
    "labeled_statement": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                             "+", "-", "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char",
                             "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union",
                             "enum", "EOF", "case", "default", "if", "switch", "while", "do", "for", "goto",
                             "continue", "break", "return"],
    "compound_statement": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                              "+", "-", "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char",
                              "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union",
                              "enum", "EOF", "case", "default", "if", "switch", "while", "do", "for", "goto",
                              "continue", "break", "return"],
    "declaration_list": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                            "+", "-", "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char",
                            "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union",
                            "enum", "EOF"],
    "statement_list": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                           "+", "-", "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char",
                           "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union",
                           "enum", "EOF"],
    "expression_statement": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                                 "+", "-", "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char",
                                 "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union",
                                 "enum", "EOF", ";"],
    "selection_statement": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                               "+", "-", "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char",
                               "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union",
                               "enum", "EOF", "if", "switch"],
    "iteration_statement": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                               "+", "-", "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char",
                               "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union",
                               "enum", "EOF", "while", "do", "for"],
    "jump_statement": ["IDENTIFIER", "CONSTANT", "STRING_LITERAL", "GET", "'('", "sizeof", "++", "--", "&", "*",
                           "+", "-", "~", "!", "typedef", "extern", "static", "auto", "register", "void", "char",
                           "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union",
                           "enum", "EOF", "goto", "continue", "break", "return"],
    "translation_unit": ["EOF"],
    "external_declaration": ["EOF"],
    "function_definition": ["EOF"]
}

# Function to compute the FIRST set for a given non-terminal

def first(non_terminal):
    first_set = set()
    if non_terminal in terminals:
        first_set.add(non_terminal)
        return first_set
    for production in grammar_rules[non_terminal]:
        if production == "EPSILON":
            first_set.add("EPSILON")
        else:
            i = 0
            while i < len(production):
                first_set |= first(production[i])
                if "EPSILON" not in first(production[i]):
                    break
                i += 1
            else:
                first_set.add("EPSILON")
    return first_set

# Function to compute the FOLLOW set for a given non-terminal

def follow(non_terminal):
    follow_set = set()
    if non_terminal == "translation_unit":
        follow_set.add("EOF")
    for key, value in grammar_rules.items():
        for prod in value:
            idx = 0
            while idx < len(prod):
                if prod[idx] == non_terminal:
                    if idx == len(prod) - 1:
                        if key != non_terminal:
                            follow_set |= follow(key)
                    else:
                        if prod[idx + 1] in terminals:
                            follow_set.add(prod[idx + 1])
                        else:
                            first_of_next = first(prod[idx + 1])
                            if "EPSILON" in first_of_next:
                                follow_set |= first_of_next - {"EPSILON"}
                                if key != non_terminal:
                                    follow_set |= follow(key)
                            else:
                                follow_set |= first_of_next
                idx += 1
    return follow_set

# Construct the parsing table
parsing_table = {}
for non_terminal in non_terminals:
    for production in grammar_rules[non_terminal]:
        if production != "EPSILON":
            for terminal in first(production[0]):
                if terminal != "EPSILON":
                    if (non_terminal, terminal) in parsing_table:
                        print("Grammar is not LL(1): Multiple entries for non-terminal", non_terminal, "and terminal", terminal)
                    else:
                        parsing_table[(non_terminal, terminal)] = production
        else:
            for terminal in follow(non_terminal):
                if (non_terminal, terminal) in parsing_table:
                    print("Grammar is not LL(1): Multiple entries for non-terminal", non_terminal, "and terminal", terminal)
                else:
                    parsing_table[(non_terminal, terminal)] = production

# Print the parsing table
print(parsing_table.items())
for i in parsing_table.items():
     print(i)
print("Predictive Parsing Table:")
print("----------------------------")
for key, value in parsing_table.items():
    print(key, ":", value)
