from search import search_prompt

def main():
    print("Chat iniciado! Digite sua pergunta (ou 'sair' para encerrar):")
    
    while True:
        question = input("\nPergunta: ").strip()
        
        if question.lower() in ['sair', 'exit', 'quit']:
            print("Encerrando chat...")
            break
        
        if not question:
            print("Por favor, digite uma pergunta.")
            continue
        
        try:
            response = search_prompt(question)
            print(f"\nResposta: {response}")
        except Exception as e:
            print(f"Erro ao processar pergunta: {e}")

if __name__ == "__main__":
    main()