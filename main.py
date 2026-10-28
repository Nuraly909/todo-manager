tasks = []


def add_task(title):
    """Тізімге жаңа тапсырма қосады."""
    if not title.strip():
        print("Атауы бос болмауы керек")
        return
    tasks.append({"title": title, "done": False})


if __name__ == "__main__":
    add_task("Бірінші тапсырма")
    print(tasks)
