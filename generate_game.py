import json
import os
import argparse
import math

def create_dashboard(progress, ai_mood, coffee, location):
    """Creates the formatted dashboard string for a node."""
    progress = max(0, min(100, progress))
    coffee = max(0, min(100, coffee))
    progress_bar = '█' * int(20 * progress / 100) + '░' * (20 - int(20 * progress / 100))
    coffee_bar = '█' * int(20 * coffee / 100) + '░' * (20 - int(20 * coffee / 100))
    line1 = f"| MISSION PROGRESS: [{progress_bar}] {progress}%"
    line2 = f"| COFFEE LEVEL:     [{coffee_bar}] {coffee}%"
    line3 = f"| SHIP'S AI MOOD:   {ai_mood}"
    line4 = f"| LOCATION:         {location}"
    return (
        "```\n"
        "========================================================================\n"
        f"{line1.ljust(79)}|\n"
        f"{line2.ljust(79)}|\n"
        f"{line3.ljust(79)}|\n"
        f"{line4.ljust(79)}|\n"
        "========================================================================\n"
        "```"
    )

def create_choices_markdown(choices, current_stage):
    """Creates the Markdown formatted list of choices with stage-aware linking."""
    if not choices:
        return ""

    choice_links = []
    for choice in choices:
        target_node_id = choice['target_node_id']
        target_stage = math.ceil(target_node_id / 50) # Assuming 50 nodes per stage

        if target_stage == current_stage:
            link_path = f"./README-{str(target_node_id).zfill(4)}.md"
        else:
            link_path = f"../stage-{str(target_stage).zfill(2)}/README-{str(target_node_id).zfill(4)}.md"

        choice_links.append(f"*   [{choice['text']}]({link_path})")

    return "\n".join(choice_links)

def generate_node_file(node, current_stage):
    """Generates the full Markdown content for a single node and saves it to a file."""
    dashboard_data = node.get('dashboard_update', {})
    dashboard_md = create_dashboard(
        dashboard_data.get('mission_progress', 0),
        dashboard_data.get('ai_mood', 'Nominal'),
        dashboard_data.get('coffee_level', 50),
        node.get('location', 'Unknown')
    )

    puzzle_md = ""
    if node.get('puzzle'):
        puzzle = node['puzzle']
        puzzle_md = f"### {puzzle.get('type', 'Puzzle')}\n\n{puzzle.get('text', '')}\n\n{puzzle.get('data', '')}"

    choices_md = create_choices_markdown(node.get('choices', []), current_stage)

    content = (
        f"<h1 align=\"center\">A Day in the Life of a Space Programmer</h1>\n\n"
        f"---\n\n"
        f"<h2 id=\"node-{node['node_id']}\">{node['title']}</h2>\n\n"
        f"{dashboard_md}\n\n"
        f"{node['story_text']}\n\n"
        f"{puzzle_md}\n\n"
        f"### Your Choices\n\n"
        f"{choices_md}\n"
    )

    stage_dir = f"stage-{str(current_stage).zfill(2)}"
    if not os.path.exists(stage_dir):
        os.makedirs(stage_dir)
        # Create a .gitkeep to ensure the directory is tracked if it's empty
        with open(os.path.join(stage_dir, '.gitkeep'), 'w') as f:
            pass

    filename = f"README-{str(node['node_id']).zfill(4)}.md"
    filepath = os.path.join(stage_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """Main function to generate game files for a specific stage."""

    parser = argparse.ArgumentParser(description="Generate game files for a specific stage.")
    parser.add_argument('--stage', type=int, required=True, help='The stage number to generate.')
    parser.add_argument('--nodes-per-stage', type=int, default=50, help='Number of nodes per stage.')
    args = parser.parse_args()

    try:
        with open('story_graph.json', 'r', encoding='utf-8') as f:
            story_data = json.load(f)
    except FileNotFoundError:
        print("Error: story_graph.json not found.")
        return

    all_nodes = story_data.get('nodes', [])
    if not all_nodes:
        print("No nodes found in story_graph.json.")
        return

    start_node_id = ((args.stage - 1) * args.nodes_per_stage) + 1
    end_node_id = args.stage * args.nodes_per_stage

    nodes_to_generate = [node for node in all_nodes if start_node_id <= node['node_id'] <= end_node_id]

    if not nodes_to_generate:
        print(f"No nodes found for Stage {args.stage}.")
        return

    for node in nodes_to_generate:
        generate_node_file(node, args.stage)

    print(f"Successfully generated {len(nodes_to_generate)} node files for Stage {args.stage}.")

if __name__ == '__main__':
    main()
