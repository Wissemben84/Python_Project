import hashlib


wordlist_user = r"C:\Users\wissem\OneDrive - Groupe ESAIP\Bureau\mes_programmes_python\crack de mot de passe\rockyou.txt" #chemin de la wordlist à changer
while True:
    try:
        wordlist = open(wordlist_user, 'r', encoding='utf-8', errors='ignore')
        hash_input = input("veuillez fournir votre hash : ")
        choix = input("faites votre choix de mode : md5\n sha1\n sha224\n sha256\n sha384\n sha512\n blake2b\n blake2s\n ")

        # Parcours de chaque ligne de la liste
        for word in wordlist:
            word = word.strip()  # supprime les espaces et sauts de lignes
            match choix:
                case "SHA1" | "sha1":
                    wordlist_hash = hashlib.sha1(word.encode('utf-8')).hexdigest()
                case "MD5" | "md5":
                    wordlist_hash = hashlib.md5(word.encode('utf-8')).hexdigest()
                case "SHA224" | "sha224":
                    wordlist_hash = hashlib.sha224(word.encode('utf-8')).hexdigest()
                case "SHA256" | "sha256":
                    wordlist_hash = hashlib.sha256(word.encode('utf-8')).hexdigest()
                case "SHA512" | "sha512":
                    wordlist_hash = hashlib.sha512(word.encode('utf-8')).hexdigest()
                case "SHA384" | "sha384":
                    wordlist_hash = hashlib.sha384(word.encode('utf-8')).hexdigest()
                case "blake2b" | "BLAKE2b":
                    wordlist_hash = hashlib.blake2b(word.encode('utf-8')).hexdigest()
                case "blake2s" | "BLAKE2s":
                    wordlist_hash = hashlib.blake2s(word.encode('utf-8')).hexdigest()
                case _:
                    print("Le choix n'est pas valide")
            if hash_input == wordlist_hash:
                print('MOT DE PASSE TROUVée ==> ' + word)
                break
            else:
                print('Pas de mot de passe trouvé')

        wordlist.close()

    except FileNotFoundError:
        print("Le fichier n'existe pas !!!\n")
    except UnicodeDecodeError:
        print('Erreur de décodage du fichier. Vérifiez bien l\'encodage du fichier.\n')
    break
