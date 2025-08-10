<h1 align="center">A Day in the Life of a Space Programmer</h1>

---

<h2 id="node-2">☕ 08:00 - The First Task</h2>

```
========================================================================
| MISSION PROGRESS: [█░░░░░░░░░░░░░░░░░░░] 5%                                  |
| COFFEE LEVEL:     [████████████████████] 100%                                |
| SHIP'S AI MOOD:   Sarcastic                                                  |
| LOCATION:         Mess Hall                                                  |
========================================================================
```

You shuffle into the mess hall. Your manager, a perpetually cheerful avatar named "Manager Mike," hovers over the central table.

"Gooood morning, team!" he chirps. "Big day today! We've got a critical issue in the Nutrient Paste Dispenser. It's stuck in a recursive loop and is threatening to fill the entire station with a lukewarm, grey blob. It's also, and this is the important part, the same machine that dispenses the coffee. This is a Code Red, people!"

STEVe chimes in, "He's not wrong. My projections show that at the current rate of expansion, the grey blob will achieve sentience in approximately 47 hours."

Manager Mike ignores him. "I've uploaded the core dispenser logic to your terminals. Find the bug and fix it! The fate of our coffee depends on you!"

### code_bug

"The function is called with `dispensePaste(10)`," Mike adds. "Find the line with the bug!"

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

### Your Choices

*   [The bug is `if (amount <= 0)`. It should be `if (amount == 0)`.](./README-0003.md)
*   [The bug is `dispensePaste(amount);`. It should be `dispensePaste(amount - 1);`.](./README-0004.md)
