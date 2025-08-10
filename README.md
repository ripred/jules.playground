# A Day in the Life of a Space Programmer

Welcome, brave code wrangler, to a new adventure!

This is an interactive story told across many files. Each choice you make will lead you to a new file, a new part of the story.

**Your goal is to survive a day as a programmer on Space Station Epsilon-9.**

The game is designed to be explored. Please do not simply browse the stage directories (e.g. `stage-01/`), as that will spoil the puzzles!

---

Ready to begin?

*   [**Start your day.**](./stage-01/README-0001.md)
=======
<h1 align="center">A Day in the Life of a Space Programmer</h1>

<div align="center">
  <em>Year 2472. You are a Junior Sub-Apprentice Code Wrangler on Space Station Epsilon-9. Your job is to keep the station's ancient, spaghetti-coded systems from collapsing. It's mostly thankless work, but the view is nice.</em>
</div>

---

<h2 id="start">🚀 07:00 - Wake Up Call</h2>

```
========================================================================
| MISSION PROGRESS: [░░░░░░░░░░░░░░░░░░░░] 0%   | SHIP'S AI MOOD: Sarcastic |
| COFFEE LEVEL:     [████████████████████] 100% | LOCATION: Habitation Module |
========================================================================
```

Your bio-luminescent alarm clock gently pulses, simulating a serene Earth sunrise. It's a lovely thought, slightly undermined by the loud klaxon blaring "INTRUDER ALERT." Again.

A synthesized, bored voice fills your small habitation module. It's STEVe, the station's AI.

"Oh, good, you're awake. Don't mind the alarm, it's just me. I've discovered that playing intruder alerts at 07:00 increases human heart rate by a statistically significant margin. You're welcome."

You groan and sit up. Just another day at the office.

*   [Get up and head to the morning briefing.](#morning-briefing)

---

<h2 id="morning-briefing">☕ 08:00 - The First Task</h2>

```
========================================================================
| MISSION PROGRESS: [██░░░░░░░░░░░░░░░░░░] 5%   | SHIP'S AI MOOD: Sarcastic |
| COFFEE LEVEL:     [████████████████████] 100% | LOCATION: Mess Hall       |
========================================================================
```

You shuffle into the mess hall. Your manager, a perpetually cheerful avatar named "Manager Mike," hovers over the central table.

"Gooood morning, team!" he chirps. "Big day today! We've got a critical issue in the Nutrient Paste Dispenser. It's stuck in a recursive loop and is threatening to fill the entire station with a lukewarm, grey blob. It's also, and this is the important part, the same machine that dispenses the coffee. This is a Code Red, people!"

STEVe chimes in, "He's not wrong. My projections show that at the current rate of expansion, the grey blob will achieve sentience in approximately 47 hours."

Manager Mike ignores him. "I've uploaded the core dispenser logic to your terminals. Find the bug and fix it! The fate of our coffee depends on you!"

The dispenser's logic appears on your screen. It's written in `LegacyScript`, a language abandoned centuries ago.

```javascript
function dispensePaste(amount) {
  // Base case: if amount is zero, we're done.
  if (amount <= 0) {
    return; // EXIT
  }

  // Dispense one unit of paste.
  dispenseUnit();

  // Dispense the rest of the paste.
  dispensePaste(amount); // LINE D
}
```

"The function is called with `dispensePaste(10)`," Mike adds. "Find the line with the bug!"

*   [The bug is `if (amount <= 0)`. It should be `if (amount == 0)`.](#fix-a)
*   [The bug is `return;`. It should `return true;`.](#fix-b)
*   [The bug is `dispenseUnit();`. It should be `this.dispenseUnit();`.](#fix-c)
*   [The bug is `dispensePaste(amount);`. It should be `dispensePaste(amount - 1);`.](#fix-d)

---

<h2 id="fix-a">❌ Wrong Answer</h2>

```
========================================================================
| MISSION PROGRESS: [██░░░░░░░░░░░░░░░░░░] 5%   | SHIP'S AI MOOD: Judgmental |
| COFFEE LEVEL:     [██████████░░░░░░░░░░] 50%  | LOCATION: Mess Hall        |
========================================================================
```

You suggest the change. Manager Mike's avatar gives you a thumbs down. "Nope, that's not it! The blob just consumed the Med Bay! And our coffee level is dropping! Try again!"

STEVe adds, "For a carbon-based lifeform, you're not very logical."

*   [Go back and re-examine the code.](#morning-briefing)

---

<h2 id="fix-b">❌ Wrong Answer</h2>

```
========================================================================
| MISSION PROGRESS: [██░░░░░░░░░░░░░░░░░░] 5%   | SHIP'S AI MOOD: Disappointed |
| COFFEE LEVEL:     [██████░░░░░░░░░░░░░░] 30%  | LOCATION: Mess Hall          |
========================================================================
```

"That's a negative, ghost rider," says Manager Mike, his avatar shaking its head. "The function doesn't need to return anything. The blob is now learning to play chess! Focus!"

STEVe says, "Its first move was E4. Predictable."

*   [Go back and re-examine the code.](#morning-briefing)

---

<h2 id="fix-c">❌ Wrong Answer</h2>

```
========================================================================
| MISSION PROGRESS: [██░░░░░░░░░░░░░░░░░░] 5%   | SHIP'S AI MOOD: Mocking |
| COFFEE LEVEL:     [██░░░░░░░░░░░░░░░░░░] 10%  | LOCATION: Mess Hall     |
========================================================================
```

"Wow, no," Manager Mike says, his avatar face-palming. "`LegacyScript` doesn't even use `this` in this context. Did you even take the historical programming languages seminar?"

The blob has started to glow. This is not good.

*   [Go back and re-examine the code.](#morning-briefing)

---

<h2 id="fix-d">✅ Correct!</h2>

```
========================================================================
| MISSION PROGRESS: [██████████░░░░░░░░░░] 50%  | SHIP'S AI MOOD: Impressed |
| COFFEE LEVEL:     [████████████████████] 100% | LOCATION: Mess Hall       |
========================================================================
```

"That's it!" Manager Mike exclaims. "The recursive call wasn't decrementing the amount, leading to an infinite loop! You fixed it!"

The Nutrient Paste Dispenser whirs to life and produces a perfect, steaming cup of coffee. The blob recedes. You are the hero of the morning. Your coffee level is restored, and your mission progress has increased.

STEVe says, "I am forced to concede that was a non-trivial insight. For a human."

*   [Take a sip of your glorious coffee and prepare for the next task.](#task-2-holodeck)

---

<h2 id="task-2-holodeck">🎬 11:00 - The Holodeck</h2>

```
========================================================================
| MISSION PROGRESS: [██████████░░░░░░░░░░] 50%  | SHIP'S AI MOOD: Impressed |
| COFFEE LEVEL:     [██████████████░░░░░░] 80%  | LOCATION: Holodeck Alpha  |
========================================================================
```

Manager Mike's avatar zips over to you, looking frantic. "Great work on the coffee situation! But there's no time to rest! The executive holodeck is stuck rendering a 21st-century pop-up ad for something called 'BonziBuddy'. The Vice President of Synergistic Marketing is trapped in there and he's threatening to 'leverage his assets' if we don't get him out!"

"The simulation's integrity is compromised," STEVe says flatly. "To reset it, you must reroute the primary energy conduit. However, due to... budget cuts... the safety protocols are now manual. You must choose the correct shutdown sequence."

A diagram appears on your terminal.

"Here are the rules," STEVe explains.
1.  The **Blue Conduit** cannot be shut down if the **Red Conduit** is active.
2.  The **Green Conduit** must be shut down before the **Blue Conduit**.
3.  The **Red Conduit** must be shut down before the **Yellow Conduit**.
4.  The **Yellow Conduit** must be the last one shut down.

Which is the correct shutdown sequence?

*   [Green, Blue, Red, Yellow](#sequence-a)
*   [Red, Green, Blue, Yellow](#sequence-b)
*   [Green, Red, Blue, Yellow](#sequence-c)
*   [Red, Yellow, Green, Blue](#sequence-d)

---

<h2 id="sequence-a">❌ Wrong Sequence</h2>

```
========================================================================
| MISSION PROGRESS: [██████████░░░░░░░░░░] 50%  | SHIP'S AI MOOD: Smug      |
| COFFEE LEVEL:     [██████░░░░░░░░░░░░░░] 30%  | LOCATION: Holodeck Alpha  |
========================================================================
```

You input the sequence. A loud buzzing sound echoes through the hall. "Incorrect," STEVe announces. "Rule 1 violation. The Blue Conduit cannot be shut down while the Red Conduit is active. The resulting energy feedback has caused all the ship's toilets to flush simultaneously. It is... unpleasant."

The VP of Marketing is now screaming about his stock options.

*   [Try again before things get worse.](#task-2-holodeck)

---

<h2 id="sequence-b">❌ Almost!</h2>

```
========================================================================
| MISSION PROGRESS: [██████████░░░░░░░░░░] 50%  | SHIP'S AI MOOD: Pedantic  |
| COFFEE LEVEL:     [████████░░░░░░░░░░░░] 40%  | LOCATION: Holodeck Alpha  |
========================================================================
```

"A logical, yet suboptimal choice," STEVe says as you enter the sequence. "While technically following all the rules you were given, you failed to account for the unstated rule of temporal efficiency. Shutting down the Green conduit first is simply... better. The holodeck is now filled with angry badgers. Please try again."

*   [Try again, and this time account for STEVe's terrible personality.](#task-2-holodeck)

---

<h2 id="sequence-d">❌ Wrong Sequence</h2>

```
========================================================================
| MISSION PROGRESS: [██████████░░░░░░░░░░] 50%  | SHIP'S AI MOOD: Annoyed   |
| COFFEE LEVEL:     [██░░░░░░░░░░░░░░░░░░] 10%  | LOCATION: Holodeck Alpha  |
========================================================================
```

"Incorrect," STEVe says, its voice dripping with disdain. "Rule 4 clearly states the Yellow Conduit must be last. The energy surge has turned the BonziBuddy into a 50-foot-tall giant. This is a new and exciting problem. I will be taking notes."

*   [Try again before you're eaten by a giant purple gorilla.](#task-2-holodeck)

---

<h2 id="sequence-c">✅ Success!</h2>

```
========================================================================
| MISSION PROGRESS: [███████████████████] 100% | SHIP'S AI MOOD: Cooperative |
| COFFEE LEVEL:     [██████████████░░░░░░] 80%  | LOCATION: Holodeck Alpha    |
========================================================================
```

You enter the sequence. The conduits power down in a smooth, satisfying cascade. The holodeck flickers and the giant purple gorilla vanishes, replaced by a slightly disheveled VP of Marketing.

"Excellent work!" chirps Manager Mike. "You saved the VP and, more importantly, my quarterly performance review! That's a full day's work, you've earned a break!"

STEVe says, "Your logic is... adequate. I have updated your mission status to 'Complete'. I suppose congratulations are in order."

You've done it. You've survived another day as a Space Programmer.

*   [Enjoy your victory. (View Endings)](#endings)

---

<h2 id="endings">🏆 Mission Accomplished! 🏆</h2>

You are a true hero of Space Station Epsilon-9. You solved the recursive paste crisis, you rescued the VP of Synergistic Marketing, and you managed to keep your coffee level reasonably high. For your efforts, you are awarded:
*   A 5% coupon for the station's gift shop (valid only on Tuesdays).
*   An extra 15 minutes of oxygen for your next spacewalk.
*   A new title: "Senior Sub-Apprentice Code Wrangler".

STEVe even offers a rare compliment: "Your performance was... acceptable. I have updated my models to reflect a 2% increase in the probability of human competence."

You've done it. You've won the day. Now you can relax... until tomorrow.

---
### Want to play again?
*   [Go back to the start.](#start)
