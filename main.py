from questions import questions

print("🚀 Welcome to Astreon Expedition 🚀")
print("----------------------------------")

score = 0
parts = 0

for q in questions:
    print("\n" + q["question"])

    for i, choice in enumerate(q["choices"]):
        print(f"{i+1}. {choice}")

    answer = int(input("Your answer (1-4): ")) - 1

    if answer == q["answer"]:
        print("✅ Correct! You collected a spaceship part.")
        score += 1
        parts += 1
    else:
        print("❌ Wrong answer.")

print("\n🎉 Mission Complete!")
print("Score:", score)
print("Spaceship parts collected:", parts)

if parts >= 2:
    print("🚀 Ship assembled! You can travel to the next planet!")
else:
    print("🔧 Ship incomplete. Try again!")
