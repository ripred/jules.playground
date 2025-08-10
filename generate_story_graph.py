import json
import random
import argparse
import math

# --- Content Pools for Procedural Generation ---

SYSTEMS = [
    "Cryo-Sleep Chamber", "Nutrient Paste Dispenser", "Holodeck Projector",
    "Grav-Plating Stabilizer", "Oxygen Scrubber", "Laser Turret AI",
    "Quantum Carburetor", "Warp Field Regulator", "Shield Modulator",
    "Escape Pod Launch System", "Trash Compactor", "Ship's Main AI Core"
]

VERBS_BROKEN = [
    "is malfunctioning", "has gone rogue", "is stuck in a recursive loop",
    "is emitting strange noises", "is printing endless gibberish",
    "is refusing to authenticate", "has developed a superiority complex",
    "is leaking a viscous fluid", "is haunted by a digital ghost"
]

VERBS_FIX = [
    "re-calibrate the", "de-frag the", "purge the cache of the",
    "re-align the", "debug the", "pacify the", "un-haunt the",
    "perform a hard reset on the", "decode the error logs from the"
]

AI_MOODS = ["Sarcastic", "Annoyed", "Judgmental", "Impressed", "Cooperative", "Pedantic", "Smug", "Nominal"]

# --- Main Generation Logic ---

def generate_story_graph(num_nodes, nodes_per_stage):
    """
    Generates a complex, web-like story graph with the specified number of nodes.
    """
    nodes = []

    # Create the starting node
    nodes.append({
        "node_id": 1,
        "stage": 1,
        "title": "🚀 07:00 - Wake Up Call",
        "location": "Habitation Module",
        "story_text": "A synthesized, bored voice fills your small habitation module. It's STEVe, the station's AI.\n\n\"Oh, good, you're awake. I've taken the liberty of preemptively debugging the coffee machine. You're welcome.\"",
        "puzzle": None,
        "choices": [], # Will be populated as we build the graph
        "dashboard_update": {"mission_progress": 0, "ai_mood": "Sarcastic", "coffee_level": 100}
    })

    # Build the graph node by node
    for i in range(2, num_nodes + 1):
        current_stage = math.ceil(i / nodes_per_stage)

        # Find a random parent node to link from.
        potential_parents = [n for n in nodes if len(n.get("choices", [])) < 4 and n.get("title") != "🏆 Game Over" and n.get("node_id") < i]
        if not potential_parents:
            potential_parents = [n for n in nodes if n.get("title") != "🏆 Game Over" and n.get("node_id") < i]
        parent_node = random.choice(potential_parents) if potential_parents else nodes[-1]

        system = random.choice(SYSTEMS)
        broken_verb = random.choice(VERBS_BROKEN)
        fix_verb = random.choice(VERBS_FIX)

        title = f"💥 Critical Alert: {system}"
        story_text = f"STEVe's voice crackles over the comms. \"Great. Now the {system} {broken_verb}. You should probably go and {fix_verb} {system}.\""

        new_choices = []
        # If this is the last node of a stage (and not the final node), link to the next stage
        if i % nodes_per_stage == 0 and i < num_nodes:
            title = f"🎉 Stage {current_stage} Complete!"
            story_text = "You've handled the immediate crises. Time to move to the next sector of the station and see what else is on fire."
            new_choices.append({"text": f"Proceed to Stage {current_stage + 1}", "target_node_id": i + 1})
        elif i >= num_nodes - 5: # Make the last 5 nodes endings
            title = "🏆 Game Over"
            story_text = "The station is either saved or doomed, but your shift is over. You've seen things... strange things."
            new_choices.append({"text": "Play again.", "target_node_id": 1})
        else: # A regular node with complex choices
            # 1. Forward choice (progress)
            forward_target = min(num_nodes, i + random.randint(1, 5))
            new_choices.append({"text": f"Attempt to {fix_verb} {system}.", "target_node_id": forward_target})

            # 2. Cross-link choice (side quest)
            cross_link_target = random.randint(max(1, i-20), min(num_nodes, i+20))
            if cross_link_target != i: # Avoid linking to self
                new_choices.append({"text": f"Check status of the {random.choice(SYSTEMS)}.", "target_node_id": cross_link_target})

            # 3. Loop choice (go back)
            if i > 10:
                loop_target = i - random.randint(1, 5)
                new_choices.append({"text": "Wait, what was that first thing again?", "target_node_id": loop_target})

        new_node = {
            "node_id": i,
            "stage": current_stage,
            "title": title,
            "location": random.choice(["Engineering", "Bridge", "Mess Hall", "Cargo Bay", "The Vents"]),
            "story_text": story_text,
            "puzzle": None,
            "choices": new_choices,
            "dashboard_update": {
                "mission_progress": int((i / num_nodes) * 100),
                "ai_mood": random.choice(AI_MOODS),
                "coffee_level": max(0, 100 - int((i / num_nodes) * 95))
            }
        }
        nodes.append(new_node)

        # Add a choice in the parent node that points to this new node
        if parent_node["node_id"] != i: # A node can't be its own parent
            parent_node["choices"].append({
                "text": f"Investigate the alert about the {system}.",
                "target_node_id": i
            })

    return {"nodes": nodes}

def main():
    """
    Main function to generate the story graph and save it to a file.
    """
    parser = argparse.ArgumentParser(description="Generate a story graph for a multi-stage game.")
    parser.add_argument('--nodes', type=int, default=1001, help='Total number of nodes to generate.')
    parser.add_argument('--nodes-per-stage', type=int, default=50, help='Number of nodes per stage.')
    args = parser.parse_args()

    story_graph = generate_story_graph(args.nodes, args.nodes_per_stage)

    with open('story_graph.json', 'w') as f:
        json.dump(story_graph, f, indent=2)

    print(f"Generated a new story_graph.json with {len(story_graph['nodes'])} nodes across {math.ceil(args.nodes / args.nodes_per_stage)} stages.")

if __name__ == '__main__':
    main()
