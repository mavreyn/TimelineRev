'''
Literally just takes my timeline and reveals it back to me token by token
The magic to make it happen

This is actually super sick I got the line restarter working holy moly!!
Now I can have a score count and make it like a game (lower score is better)

Maverick Reynolds
02.27.2023

▁▂▃▄▅▆▇█
'''

from blessed import Terminal

def main():     
    term = Terminal()
    end = False
    inp = ''
    line_reviews = 0        # Make it a game haha
    num_lines_studied = 0
    start_ln = 0

    start = input('> ')

    with open('AMH Study 3-27.txt') as f:
        raw = f.readlines()
        total_lines = len(raw)

    if start:
        # Find first line with the given information and start from there
        for i, line in enumerate(raw):
            if start in line.lower():
                prev, raw = raw[i-5:i], raw[i:]    # Split on i
                print('\t\t.\n\t\t.\n\t\t.')
                start_ln = i
                break

        for line in prev:
            print(line, end='')
        print()


    # Begin loop for desired poetion
    for line in raw:
        running_len = 0
        restart = True

        # To escape outer loop
        if end:
            break

        # Repeat as long as the user presses space to request restart
        while restart and not end:
            restart = False

            for token in line.split(' '):
                print(term.move_up, end='')

                if inp == ' ':
                    # Clear the line then go back to the start
                    print(term.clear_eol + '\r', end='')
                    running_len = 0
                else:
                    # move_right(0) still moves right, so small condition required
                    print(term.move_right(-1 if running_len == 0 else running_len), end='')

                # Print the token
                running_len += len(token) + 1
                inp = input(token)

                # Alternate inputs
                if inp == ' ':
                    restart = True
                    line_reviews += 1
                    break
                elif inp == 'END':
                    end = True
                    break
        
        num_lines_studied += 1


    # Make end display
    end_card_width = 43

    # Perform calculation to show section studied
    st_disp = int(start_ln/total_lines * (end_card_width-2))
    end_disp = int((start_ln + num_lines_studied)/total_lines * (end_card_width-2))
    
    print('\n=================== END ===================')
    print(f" Line Restarts: {line_reviews:26}")
    print(f" Number of Line Studied: {num_lines_studied:17}")
    print(f" Percent Reviewed:  {num_lines_studied / total_lines * 100:21.2f}%")
    print()

    # Print the range display
    for i in range(end_card_width):
        if i == 0:
            print('├', end='')
        elif i == end_card_width - 1:
            print('┤')
        elif st_disp <= i <= end_disp:
            print('■', end='')
        else:
            print('─', end='')

    print('\n===========================================')
    input()    

        

if __name__ == '__main__':
    main()

