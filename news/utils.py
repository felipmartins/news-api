import json
from random import choice, randint


def generate_data():
    result = []
    id = 1

    authors = [
        "Lorem Nullam",
        "Maecenas Aliquam",
        "Aliquam Nam",
        "Finibus Bonorum",
        "Nulla Feugiat",
    ]

    categories = ["ferramentas", "tecnologia", "carreira"]

    titles_suffix = [
        "Maecenas varius laoreet ligula eget consequat. Sed.",
        "Nunc pulvinar lorem ac sem convallis, vel.",
        "Etiam dui ante, mollis eget venenatis eget.",
        "Proin eget erat ultricies, pretium lacus et.",
        "Aenean id imperdiet nisl, cursus elementum metus.",
    ]

    content = [
        "Vivamus nunc ligula, pharetra in ex quis, cursus feugiat nulla. Sed magna lacus, efficitur ultricies orci ut, ullamcorper euismod nunc. Nulla vel tincidunt tortor, non vulputate libero. Donec nisi turpis, faucibus sit amet tellus sit amet, facilisis mattis odio. Nam congue nunc nec erat consequat, non bibendum lectus vestibulum. Nunc blandit ullamcorper suscipit. Fusce non libero eget neque dictum pellentesque quis ac nisi. Praesent nec aliquam magna. In dolor tellus, pharetra nec ullamcorper at, cursus et dolor. Sed nec sagittis ipsum.",
        "Suspendisse et dictum velit, eget hendrerit odio. Pellentesque fringilla, felis eget hendrerit lacinia, enim purus ultrices enim, id pharetra ante urna quis magna. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam sollicitudin in augue eget blandit. Aenean consectetur eleifend tincidunt. Nunc varius diam eget odio efficitur rhoncus. Vestibulum ex erat, tristique ut aliquet eget, gravida nec mi. Proin tincidunt, nunc id ornare mattis, sapien augue egestas neque, sit amet luctus libero nulla in arcu. Maecenas elementum risus a vulputate feugiat. Sed tempor quis nibh sed elementum. Cras volutpat, ante ac sollicitudin consectetur, tellus nisl hendrerit tellus, vestibulum hendrerit massa risus ut ante. Curabitur placerat orci metus. Duis eu nisi nec libero blandit bibendum nec ac neque. Donec tincidunt turpis eu nisl suscipit, et tincidunt justo suscipit. Suspendisse auctor commodo felis iaculis vulputate.",
        "Aliquam aliquam metus in mi hendrerit porttitor id at augue. Proin finibus imperdiet vestibulum. Proin ex velit, tincidunt id ultrices non, suscipit sed nunc. Nulla lobortis gravida diam, et venenatis orci semper vitae. Aenean non ante fringilla, lacinia risus et, posuere felis. Proin augue ligula, interdum eu gravida ac, sodales sed mi. Nullam non mauris tincidunt, molestie lorem in, varius nisl. Aliquam mattis justo lorem, sit amet ornare dui venenatis sed. Sed nulla lacus, consequat non metus ut, ultricies malesuada orci. Etiam scelerisque egestas eros sed venenatis.",
        "Mauris pellentesque nunc nec odio eleifend, maximus tincidunt odio pretium. Sed congue arcu vel massa condimentum, vel dapibus augue euismod. Sed pretium turpis vitae ex sollicitudin, sed pulvinar eros mollis. Duis non elit nibh. Nulla vel nisl nec nisi mattis facilisis. Donec justo sapien, viverra nec ex nec, semper viverra tellus. Etiam sem turpis, euismod at lacinia a, mollis vitae nunc. Quisque ac purus id ligula pulvinar pretium vitae nec risus. In feugiat, odio vel dapibus sodales, diam arcu rhoncus nunc, nec dapibus arcu nibh sit amet arcu.",
        "Duis sit amet massa vitae ipsum hendrerit maximus at sed nunc. In malesuada orci dui, vitae lacinia elit blandit eget. Morbi scelerisque vulputate accumsan. Nullam volutpat nisl elit, et elementum dolor dignissim a. In mollis quam ut sapien faucibus, mollis ornare ante tincidunt. Phasellus ut risus quam. Fusce congue lacus sed justo facilisis ullamcorper. Donec nec tincidunt mi. Cras accumsan malesuada nulla sed ultrices.",
    ]

    for i in range(50):
        result.append(
            {
                "id": id,
                "author": choice(authors),
                "category": choice(categories),
                "title": f"{id} - {choice(titles_suffix)}",
                "content": choice(content),
                "timestamp": f"{randint(2020,2022)}-{randint(1,12)}-{randint(1,28)}",
            }
        )
        id += 1

    with open("mocks/news.json", mode="w") as file:
        file.write(json.dumps(result))
