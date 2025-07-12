import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)
remote_server = input('Entrez le nom de domaine/IP: ')
remote_server_IP = socket.gethostbyname(remote_server)
print('IPV4: ', remote_server_IP)

print("-"*60)
print('Veuillez patienter pendant le scan de', remote_server_IP)
print("-"*60)

t1 = datetime.now()
try:
    for port in range(79,85):                  #à changer pour scanner les ports souhaitées
        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultat = connexion.connect_ex((remote_server_IP, port))
        if resultat==0:
            print('Port {}: open'.format(port))
            connexion.close()
except KeyboardInterrupt:
    print("Vous avez interrompu le systeme en effectuant la commande ctrl+ C")
    sys.exit()
except socket.gaierror:
    print('Nom de domaine invalide. Impossible de résoudre l\'adresse.')
    sys.exit()
t2 = datetime.now()
Ttotal = t2-t1

print("-"*60)
print('Scan terminé en', Ttotal, 'secondes')
