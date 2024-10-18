import os
from translator import Translator

def main():
    # Configurações do Azure
    endpoint = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
    api_key = os.getenv("AZURE_TRANSLATOR_KEY")

    # Criação do objeto Translator
    translator = Translator(endpoint, api_key)

    # Configurações da tradução
    source_url = "https://example.com/path/to/your/document.pdf"  # URL do documento a ser traduzido
    target_language = "fr"  # Código do idioma de destino (ex: 'fr' para francês)
    display_name = "Technical Article Translation"

    # Executa a tradução
    translation_result = translator.translate_documents(source_url, target_language, display_name)

    # Verifica e imprime os resultados
    if translation_result:
        print(f"Translation job ID: {translation_result.id}")
        print("Translation status:", translation_result.status)
    else:
        print("Translation failed.")

if __name__ == "__main__":
    main()