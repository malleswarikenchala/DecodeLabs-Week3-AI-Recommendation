
print("Movie Recommendation System")

movies = {
    "action": ["John Wick", "Avengers", "Mad Max"],
    "comedy": ["3 Idiots", "Dhamaal", "Hera Pheri"],
    "romance": ["Titanic", "The Notebook", "La La Land"],
    "horror": ["The Conjuring", "Insidious", "Annabelle"]
}

choice = input("Enter your favorite genre (action/comedy/romance/horror): ").lower()

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print("-", movie)
else:
    print("Sorry, genre not found.")



