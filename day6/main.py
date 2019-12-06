def read_input():
    planets = {}

    for center, satellite in [
        l.strip().split(")")
        for l in open('input.txt')
    ]:
        if satellite not in planets:
            planets[satellite] = Planet(satellite)
        if center not in planets:
            planets[center] = Planet(center)
        planets[satellite].orbits.append(planets[center])

    return planets


def get_orbit_count(planet, planets):
    c = 0
    for p in planet.orbits:
        c += 1
        c += get_orbit_count(p, planets)
    return c


def part_1(ip):
    return sum(
        get_orbit_count(p, ip)
        for p in ip.values()
    )


def get_chain(planet, planets, depth=0):
    chain = []
    for p in planet.orbits:
        chain.append((p, depth))
        chain += get_chain(p, planets, depth + 1)
    return chain


def part_2(ip):
    you_chain = get_chain(ip["YOU"], ip)
    you_ava = {x for x, _ in you_chain}
    san_chain = get_chain(ip["SAN"], ip)
    san_ava = {x for x, _ in san_chain}
    ava = you_ava & san_ava

    def cost(x, y, s):
        c = 0
        for i, j in y:
            if i == x:
                c += j
                break
        for i, j in s:
            if i == x:
                c += j
                break
        return c

    min_cost = 9999999999999
    for p in ava:
        c = cost(p, you_chain, san_chain)
        if c < min_cost:
            min_cost = c
    return min_cost


class Planet:
    def __init__(self, name):
        self.name = name
        self.orbits = []

    def __repr__(self):
        return self.name


if __name__ == '__main__':
    print(f"Part 1: {part_1(read_input())}")
    print(f"Part 2: {part_2(read_input())}")
