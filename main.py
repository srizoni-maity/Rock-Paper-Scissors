from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

def tournament_mode():
    print("\n🤖 AI Tournament Mode 🤖")
    print("Your AI vs 4 Bots (1000 rounds each)")
    print("-" * 40)
    print("vs Quincy:", play(player, quincy, 1000))
    print("vs Abbey:", play(player, abbey, 1000))
    print("vs Kris:", play(player, kris, 1000))
    print("vs Mrugesh:", play(player, mrugesh, 1000))
    print("-" * 40)

def human_vs_ai():
    print("\n🎮 Human vs AI Mode 🎮")
    print("Enter R (Rock), P (Paper), S (Scissors), or Q to quit.")
    print("-" * 40)

    human_score, ai_score = 0, 0
    prev_play = ""

    while True:
        human = input("Your move: ").upper()
        if human == "Q":
            break
        if human not in ["R", "P", "S"]:
            print("Invalid input! Use R, P, or S.")
            continue

        ai = player(prev_play)
        prev_play = human

        print(f"AI plays: {ai}")
        if (human == "R" and ai == "S") or (human == "P" and ai == "R") or (human == "S" and ai == "P"):
            print("✅ You win this round!")
            human_score += 1
        elif human == ai:
            print("😐 It's a tie.")
        else:
            print("❌ AI wins this round!")
            ai_score += 1

        print(f"Score: You {human_score} - {ai_score} AI\n")

if __name__ == "__main__":
    print("==== Rock Paper Scissors AI Project ====")
    print("1. AI Tournament Mode")
    print("2. Human vs AI Mode")
    choice = input("Choose mode (1/2): ")

    if choice == "1":
        tournament_mode()
    elif choice == "2":
        human_vs_ai()
    else:
        print("Invalid choice. Exiting...")
