def run_simulation_cycle(user_prompt, current_state):
    # Blue Team response
    blue_strategy = blue_agent.generate_response(
        f"Given current state {current_state} and user input '{user_prompt}', "
        f"what is our adjusted strategy?"
    )
    
    # Red Team counter-moves
    red_reaction = red_agent.generate_response(
        f"The company is doing: {blue_strategy}. How do you respond?"
    )
    
    # Synthesize outcomes
    return white_cell_synthesize(blue_strategy, red_reaction, current_state)