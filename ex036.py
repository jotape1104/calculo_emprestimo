v_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Agora me informe qual o seu salário: R$'))
tempo = int(input('Agora por ultimo, Informe em quantos anos você pretende pagar essa casa: '))
prestacao = v_casa / (tempo * 12)
if prestacao > (30 * salario) / 100:
    print('EMPRÉSTIMO NEGADO')
else:
    print('PARABÉNS, seu empréstimo foi aprovado! Em {} anos você terá que pagar R${:.2f} por mês'.format(tempo, prestacao))