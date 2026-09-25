import csv
import requests


API_URL = "https://openlibrary.org/search.json"

search_params = {
    "q": "books",
    "limit": 50,
    "fields": "title,author_name,first_publish_year",
}


def get_books():
    try:
        response = requests.get(
            API_URL,
            params=search_params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get("docs", [])

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Open Library. Check your internet connection.")

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again.")

    except requests.exceptions.HTTPError as error:
        print(f"Error: Open Library returned an HTTP error: {error}")

    except requests.exceptions.JSONDecodeError:
        print("Error: Open Library returned an invalid JSON response.")

    except requests.exceptions.RequestException as error:
        print(f"Error: Request failed: {error}")

    return []


def filter_books(books):
    filtered_books = []

    for book in books:
        publish_year = book.get("first_publish_year")

        if publish_year and publish_year > 2000:
            filtered_books.append({
                "title": book.get("title", "Unknown"),
                "author": ", ".join(book.get("author_name", [])),
                "publish_year": publish_year
            })

    return filtered_books


def save_to_csv(books):
    with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:
        fieldnames = [
            "title",
            "author",
            "publish_year"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(books)


def main():
    print("Fetching books from Open Library...")

    books = get_books()

    if not books:
        print("Could not fetch books. Exiting...")
        return

    print(f"Received {len(books)} books.")

    filtered_books = filter_books(books)

    print(
        f"{len(filtered_books)} books were published after 2000."
    )

    save_to_csv(filtered_books)

    print("Books saved to books.csv")


if __name__ == "__main__":
    main()