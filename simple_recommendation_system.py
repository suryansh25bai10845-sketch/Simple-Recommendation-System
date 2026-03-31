def recommend():

    data = {
        "movies": {
            "hindi": {
                "funny": ["Hera Pheri", "Golmaal", "Bhool Bhulaiyaa"],
                "thriller": ["Drishyam", "Andhadhun", "Kahaani"],
                "horror": ["Stree", "Raaz", "Bhoot"],
                "family": ["Hum Saath Saath Hain", "Baghban", "Dangal"]
            },
            "english": {
                "funny": ["The Mask", "Mr. Bean", "Home Alone"],
                "thriller": ["Inception", "Se7en", "Gone Girl"],
                "horror": ["The Conjuring", "IT", "Annabelle"],
                "family": ["Coco", "Finding Nemo", "The Lion King"]
            }
        },

        "songs": {
            "hindi": {
                "funny": ["Bala Bala", "Aankh Marey", "Hookah Bar"],
                "thriller": ["Agar Tum Saath Ho", "Kabira", "Phir Le Aya Dil"],
                "horror": ["Naina (Raaz)", "Aami Je Tomar", "Kaun Tujhe"],
                "family": ["Tere Sang Yaara", "Dil Diyan Gallan", "Kal Ho Na Ho"]
            },
            "english": {
                "funny": ["Happy", "Can't Stop the Feeling", "Uptown Funk"],
                "thriller": ["Believer", "Radioactive", "Demons"],
                "horror": ["Thriller - Michael Jackson", "Bury a Friend", "Disturbia"],
                "family": ["Count on Me", "Perfect", "A Thousand Years"]
            }
        },

        "webseries": {
            "hindi": {
                "funny": ["Panchayat", "Gullak", "TVF Pitchers"],
                "thriller": ["Mirzapur", "Sacred Games", "Asur"],
                "horror": ["Typewriter", "Bhram", "Ghoul"],
                "family": ["Yeh Meri Family", "Home Shanti", "Gullak"]
            },
            "english": {
                "funny": ["Friends", "The Office", "Brooklyn 99"],
                "thriller": ["Breaking Bad", "Money Heist", "Dark"],
                "horror": ["The Haunting of Hill House", "Stranger Things", "Archive 81"],
                "family": ["Modern Family", "Full House", "Young Sheldon"]
            }
        },

        "videos": {
            "hindi": {
                "funny": ["Comedy Nights Clips", "Stand-up Hindi", "Funny Reels"],
                "thriller": ["Crime Stories Hindi", "Mystery Videos", "Detective Cases"],
                "horror": ["Horror Stories Hindi", "Ghost Encounters", "Scary Videos"],
                "family": ["Motivational Hindi", "Family Vlogs", "Cooking Videos"]
            },
            "english": {
                "funny": ["Try Not To Laugh", "Funny Fails", "Comedy Skits"],
                "thriller": ["Crime Documentaries", "Mystery Solved", "Detective Stories"],
                "horror": ["Scary Videos", "Paranormal Clips", "Horror Stories"],
                "family": ["Daily Vlogs", "Cooking Shows", "Motivation Videos"]
            }
        }
    }

    print("Categories: movies / songs / webseries / videos")
    category = input("Enter category: ").lower()

    print("Languages: hindi / english")
    language = input("Enter language: ").lower()

    print("Types: funny / thriller / horror / family")
    type_choice = input("Enter type: ").lower()

    try:
        recommendations = data[category][language][type_choice]
        print("\nRecommended", category.capitalize(), "in", language.capitalize(), "(", type_choice, "):")
        for item in recommendations:
            print("-", item)
    except:
        print("Sorry, no recommendations found. Please check your input.")

print("🎬 Welcome to Smart Recommendation System")
recommend()
