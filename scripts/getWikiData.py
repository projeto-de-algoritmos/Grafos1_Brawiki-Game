import wikipediaapi

def get_wikipedia_api(language='pt'):
    return wikipediaapi.Wikipedia(
        user_agent='Brawiki',
        language=language,
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )

def filter_categories(categories, forbidden_keywords):
    filtered_categories = []
    for category in categories.values():
        if not any(keyword in category.title.lower() for keyword in forbidden_keywords):
            filtered_categories.append(category)
    return filtered_categories

def get_all_pages_from_category(category, forbidden_keywords, level=0, max_level=4):
    with open('data/pt-wiki-pages.txt', "a") as output:
        for c in category.values():
            if not any(keyword in c.title.lower() for keyword in forbidden_keywords):
                output.write(f"{c.title}\n")

            if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
                 get_all_pages_from_category(c.categorymembers, forbidden_keywords, level=level + 1, max_level=max_level)

def filter_pages(input_file_path, output_file_path):
    forbidden_keywords = ["categoria", "lista", "(a)", "usuário:", "usuária:", "campeonato", "discussão", "wikipédia", "massacre", "chacina"]
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if not any(keyword in line.lower() for keyword in forbidden_keywords)]

    with open(output_file_path, 'w') as new_file:
        new_file.writelines(filtered_lines)

def remove_duplicates_pages(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    unique_sorted_lines = sorted(set(lines))

    with open(output_file_path, 'w') as output_file:
        output_file.writelines(unique_sorted_lines)

def extract_edges(input_file_path, output_file_path, wiki_api):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    with open(output_file_path, 'a') as new_file:
        for line in lines:
            page = wiki_api.page(line.rstrip())
            links = list(page.links.keys())
            new_file.write(f"{page.title}: {links}\n")

def filter_edges(input_edges_file, output_filtered_file, pages_file_path):
    with open(input_edges_file, 'r') as edges_file, open(output_filtered_file, 'w') as filtered_file, open(pages_file_path, 'r') as pages_file:
        pages_set = set(pages_file.read().splitlines())

        for line in edges_file:
            item_name, item_array = line.strip().split(':', 1)
            item_list = [elem.strip() for elem in item_array.strip("[]").split(',')]
            item_list_no_quotes = [elem.strip("'") for elem in item_list]
            filtered_list = [elem.strip() for elem in item_list_no_quotes if elem in pages_set]
            filtered_file.write(f"{item_name}:{filtered_list}\n")

def main():
    forbidden_keywords = ["portal", "predefinição", "predefinições", "!wikiprojeto", "ficheiro"]
    wiki_api = get_wikipedia_api()
    category = wiki_api.page("Categoria:Brasil")

    get_all_pages_from_category(category.categorymembers, forbidden_keywords)
    filter_pages('data/pt-wiki-pages.txt', 'data/pt-wiki-pages-without-categories-pages.txt')
    remove_duplicates_pages('data/pt-wiki-pages-without-categories-pages.txt', 'data/pt-wiki-pages-final.txt')
    extract_edges('data/pt-wiki-pages-final.txt', 'data/pt-wiki-edges.txt', wiki_api)
    filter_edges('data/pt-wiki-edges.txt', 'data/pt-wiki-edges-final.txt', 'data/pt-wiki-pages-final.txt')
    
if __name__ == "__main__":
    main()
