# assert

if __name__ == "__main__":
    try:
        assert 5 == 10, "Lo sentimos, 5 no es igual a 10"
        
        print(">>> El programa continua con su ejecución.")
    
    except AssertionError as error:
        print(error)
    