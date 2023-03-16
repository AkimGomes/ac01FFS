def analisar_notas_do_aluno(primeira_nota: float, segunda_nota: float) -> str:
    media_aluno = (primeira_nota + segunda_nota) / 2
    if media_aluno >= 7:
        resultado = "Aprovado"
    elif media_aluno >= 4:
        resultado = "DP"
    else:
        resultado = "Reprovado"

    return f"{media_aluno}, {resultado}"



