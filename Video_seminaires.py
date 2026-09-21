import random

# ==============================
# LISTE COMPLETE VERBES IRREGULIERS
# ==============================

verbes_irreguliers = {
    "arise": ("arose", "arisen", "surgir"),
    "awake": ("awoke", "awoken", "se réveiller"),
    "be": ("was/were", "been", "être"),
    "bear": ("bore", "borne", "porter / supporter"),
    "beat": ("beat", "beaten", "battre"),
    "become": ("became", "become", "devenir"),
    "begin": ("began", "begun", "commencer"),
    "bend": ("bent", "bent", "plier"),
    "bet": ("bet", "bet", "parier"),
    "bind": ("bound", "bound", "lier"),
    "bite": ("bit", "bitten", "mordre"),
    "bleed": ("bled", "bled", "saigner"),
    "blow": ("blew", "blown", "souffler"),
    "break": ("broke", "broken", "casser"),
    "bring": ("brought", "brought", "apporter"),
    "build": ("built", "built", "construire"),
    "burn": ("burnt/burned", "burnt/burned", "brûler"),
    "buy": ("bought", "bought", "acheter"),
    "catch": ("caught", "caught", "attraper"),
    "choose": ("chose", "chosen", "choisir"),
    "come": ("came", "come", "venir"),
    "cost": ("cost", "cost", "coûter"),
    "cut": ("cut", "cut", "couper"),
    "deal": ("dealt", "dealt", "traiter"),
    "dig": ("dug", "dug", "creuser"),
    "do": ("did", "done", "faire"),
    "draw": ("drew", "drawn", "dessiner"),
    "drink": ("drank", "drunk", "boire"),
    "drive": ("drove", "driven", "conduire"),
    "eat": ("ate", "eaten", "manger"),
    "fall": ("fell", "fallen", "tomber"),
    "feed": ("fed", "fed", "nourrir"),
    "feel": ("felt", "felt", "ressentir"),
    "fight": ("fought", "fought", "combattre"),
    "find": ("found", "found", "trouver"),
    "fly": ("flew", "flown", "voler"),
    "forget": ("forgot", "forgotten", "oublier"),
    "forgive": ("forgave", "forgiven", "pardonner"),
    "freeze": ("froze", "frozen", "geler"),
    "get": ("got", "got/gotten", "obtenir"),
    "give": ("gave", "given", "donner"),
    "go": ("went", "gone", "aller"),
    "grow": ("grew", "grown", "grandir"),
    "have": ("had", "had", "avoir"),
    "hear": ("heard", "heard", "entendre"),
    "hide": ("hid", "hidden", "cacher"),
    "hit": ("hit", "hit", "frapper"),
    "hold": ("held", "held", "tenir"),
    "hurt": ("hurt", "hurt", "blesser"),
    "keep": ("kept", "kept", "garder"),
    "know": ("knew", "known", "savoir"),
    "lead": ("led", "led", "diriger"),
    "leave": ("left", "left", "quitter"),
    "lend": ("lent", "lent", "prêter"),
    "let": ("let", "let", "laisser"),
    "lose": ("lost", "lost", "perdre"),
    "make": ("made", "made", "faire"),
    "mean": ("meant", "meant", "signifier"),
    "meet": ("met", "met", "rencontrer"),
    "pay": ("paid", "paid", "payer"),
    "put": ("put", "put", "mettre"),
    "read": ("read", "read", "lire"),
    "ride": ("rode", "ridden", "monter"),
    "ring": ("rang", "rung", "sonner"),
    "rise": ("rose", "risen", "se lever"),
    "run": ("ran", "run", "courir"),
    "say": ("said", "said", "dire"),
    "see": ("saw", "seen", "voir"),
    "sell": ("sold", "sold", "vendre"),
    "send": ("sent", "sent", "envoyer"),
    "set": ("set", "set", "fixer"),
    "shake": ("shook", "shaken", "secouer"),
    "shoot": ("shot", "shot", "tirer"),
    "sing": ("sang", "sung", "chanter"),
    "sit": ("sat", "sat", "s’asseoir"),
    "sleep": ("slept", "slept", "dormir"),
    "speak": ("spoke", "spoken", "parler"),
    "spend": ("spent", "spent", "dépenser"),
    "stand": ("stood", "stood", "se tenir debout"),
    "steal": ("stole", "stolen", "voler"),
    "swim": ("swam", "swum", "nager"),
    "take": ("took", "taken", "prendre"),
    "teach": ("taught", "taught", "enseigner"),
    "tell": ("told", "told", "raconter"),
    "think": ("thought", "thought", "penser"),
    "throw": ("threw", "thrown", "lancer"),
    "understand": ("understood", "understood", "comprendre"),
    "wake": ("woke", "woken", "se réveiller"),
    "wear": ("wore", "worn", "porter (vêtement)"),
    "win": ("won", "won", "gagner"),
    "write": ("wrote", "written", "écrire"),
}

# ==============================
# QUIZ
# ==============================

def quiz():
    score = 0
    verbes = list(verbes_irreguliers.items())
    random.shuffle(verbes)

    for verbe, formes in verbes[:10]:  # 10 questions
        print(f"\nVerbe: {verbe}")
        past = input("Past simple: ").strip().lower()
        participle = input("Past participle: ").strip().lower()
        traduction = input("Traduction française: ").strip().lower()

        if (past == formes[0] and
                participle == formes[1] and
                traduction == formes[2].lower()):
            print("✅ Correct !")
            score += 1
        else:
            print(f"❌ Faux.")
            print(f"Réponse: {formes[0]} - {formes[1]} - {formes[2]}")

    print(f"\n🎯 Score final: {score}/10")

quiz()
