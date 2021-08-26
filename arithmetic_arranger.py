
from pdb import Pdb

def arithmetic_arranger(problems, with_results = None):
    arranged_problems = ''
    max_lentgh = 6
    max_number_length = 4
    max_problems_allowed = 5
    spaces_between = 4
    count_problems = 0
    first_line = ''
    second_line = ''
    third_line = ''
    dashes = ''
    result = ''

    if len(problems) > max_problems_allowed:
        return 'Error: Too many problems.'

    def getDashes(max_argument_lentgh):
        return ''.join('-' * (max_lentgh - (max_number_length - max_argument_lentgh)))

    for index, problem in enumerate(problems):
        each = problem.split()
        first = each[0]
        second = each[2]
        #Start to find errors
        if len(first) > max_number_length or len(second) > max_number_length:
            count_problems += 1
            arranged_problems = 'Error: Numbers cannot be more than four digits.'
            quit
                        
        if not first.isdigit() or not second.isdigit():
            count_problems += 1
            arranged_problems = 'Error: Numbers must only contain digits.'
            quit

        if each[1] != '+' and each[1] != '-':
            count_problems += 1
            arranged_problems = 'Error: Operator must be \'+\' or \'-\'.'
            quit

        #Start to build solution
        if count_problems == 0:
            
            if len(first) > len(second):
                max_argument_length = len(first)
                dashes += getDashes(max_argument_length) + ''.join(' ' * spaces_between)
            else:
                max_argument_length = len(second)
                dashes += getDashes(max_argument_length) + ''.join(' ' * spaces_between)
            
            cant_spaces_first = max_argument_length - len(first) + 2
            first_line = first_line + ''.join(' ' * cant_spaces_first) + first + ''.join(' ' * spaces_between)
            cant_spaces_second = max_argument_length - len(second) + 1
            second_line = second_line + each[1] + ''.join(' ' * cant_spaces_second) + second +  ''.join(' ' * spaces_between)
            
            if(with_results == True):
                arithmetic_result = 0
                cant_spaces_third = 0
                if(each[1] == '+'):
                    arithmetic_result = int(first) + int(second)
                else:
                    arithmetic_result = int(first) - int(second)
                
                cant_spaces_third = max_argument_length + 2 - len(str(arithmetic_result))
                third_line = third_line + \
                    ''.join(' ' * cant_spaces_third) + \
                    str(arithmetic_result) + ''.join(' ' * spaces_between)



    result = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashes.rstrip()

    if(with_results == True):
        result += '\n' + third_line.rstrip()

    if(count_problems == 0):
        print(result)
        return result
    
    return arranged_problems
