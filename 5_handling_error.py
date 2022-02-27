while True:
    try:
        x = int(input('Enter a number : '))
        break
    except ValueError:
        print("That\'s not a valid number!")
    except KeyboardInterrupt:
        print('No input taken')
        break
    finally:
        print("\n********\n")