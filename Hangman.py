from random import randint

print('\nMid Lecture Hangman\n')
solutions = ['paris','madrid','london','toronto','sydney','moscow','oslo','tokyo','berlin','dublin']
rnum = randint(0,9)
sol = solutions[rnum]
osol = 0
osol = sol
l = len(sol)
guess = 7
sol = list(sol)
print('You have {} tries: \nX X X X X X X\n' .format(guess))
print('the word is {} letters long.'.format(l))
visual = ['_']*l
visualstr = ' '.join(visual)
print(visualstr)
l = l - 1
lstvisual = []

while (sol != ['!']*(l+1)):
    g = input('\nGuess a letter: ')
    
    if g == 'hint':
        if osol == 'paris':
            print('france')
        elif osol =='berlin':
            print('germany')
        elif osol == 'london':
            print('england')
        elif osol == 'toronto':
            print('canada')
        elif osol == 'sydney':
            print('australia')
        elif osol == 'moscow':
            print('russia')
        elif osol == 'oslo':
            print('norway')
        elif osol == 'tokyo':
            print('japan')
        elif osol == 'dublin':
            print('ireland')
        elif osol == 'madrid':
            print('spain')


    TorF = g in sol
    cnt = sol.count(g)
    visualnewstr = 0

    if TorF == False:
        guess = guess - 1

    else: 
        for iterationtimes in range(0,cnt):
            i = sol.index(g)
            visual.insert(i,g)
            del sol[i]
            sol.insert(i,'!')

            i = i+1
            del visual[i]
  
        visualnewstr = ' '.join(visual)
        print(visualnewstr)
    
    if visualnewstr != 0:
        lstvisual = list(visualnewstr)
        for rg in range(0,l):
            lstvisual.remove(' ')

    xguess = ['X']*guess 
    xguessstr = ' '.join(xguess)
    print('\n')
    print('Tries remaining:')
    print(xguessstr)
    print('\n\n\n')

    if guess == 0:
        break

if (sol == ['!']*(l+1)):
    print('\nyou win.')

print('\nPROGRAM DONE')
