def more_general(h1, h2):
    more_general_parts = []
    for x, y in zip(h1, h2):
        mg = x == "?" or (x != "0" and (x == y or y == "0"))
        more_general_parts.append(mg)
    return all(more_general_parts)

def fulfills(example, hypothesis):
   
    return more_general(hypothesis, example)

def min_generalization(h, x):
    h_new = list(h)
    for i in range(len(h)):
        if not fulfills(x[i:i+1], h[i:i+1]):
            h_new[i] = '?' if h[i] != '0' else x[i]
    return [tuple(h_new)]

def min_specialization(h, domains, x):
    results = []
    for i in range(len(h)):
        if h[i] == "?":
            for val in domains[i]:
                if x[i] != val:
                    h_new = h[:i] + (val,) + h[i+1:]
                    results.append(h_new)
        elif h[i] != "0":
            h_new = h[:i] + ('0',) + h[i+1:]
            results.append(h_new)
    return results

def get_domains(examples):
    domains = [set() for i in examples[0][:-1]]
    for x in examples:
        for i, val in enumerate(x[:-1]):
            domains[i].add(val)
    return [list(domain) for domain in domains]

def candidate_elimination(examples):
    domains = get_domains(examples)
    G = {("?",) * len(domains)}
    S = {("0",) * len(domains)}

    print("Initial G:", G)
    print("Initial S:", S)

    for x in examples:
        x_domains = x[:-1]
        if x[-1] == "yes":  # Positive example
            G = {g for g in G if fulfills(x_domains, g)}
            S = generalize_S(x_domains, S, G)
        else:  # Negative example
            S = {s for s in S if not fulfills(x_domains, s)}
            G = specialize_G(x_domains, G, S, domains)

        print("\nExample:", x)
        print("G:", G)
        print("S:", S)

    return S, G

def generalize_S(x, S, G):
    S_new = S.copy()
    for s in S:
        if not fulfills(x, s):
            S_new.remove(s)
            S_new.update([h for h in min_generalization(s, x) if any([more_general(g, h) for g in G])])
    S_new = {h for h in S_new if any([more_general(g, h) for g in G])}
    return S_new

def specialize_G(x, G, S, domains):
    G_new = G.copy()
    for g in G:
        if fulfills(x, g):
            G_new.remove(g)
            G_new.update([h for h in min_specialization(g, domains, x) if any([more_general(h, s) for s in S])])
    G_new = {h for h in G_new if any([more_general(h, s) for s in S])}
    return G_new

# Sample data
examples = [
    ('sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes'),
    ('sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes'),
    ('rainy', 'cold', 'high', 'strong', 'warm', 'change', 'no'),
    ('sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes'),
]

S, G = candidate_elimination(examples)
print("\nFinal S:", S)
print("Final G:", G)
