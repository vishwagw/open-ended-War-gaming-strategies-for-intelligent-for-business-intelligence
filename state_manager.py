class SimulationState:
    def __init__(self):
        self.timeline = {}  # Quarterly projections
        self.metrics = {
            'market_share': [],
            'revenue': [],
            'costs': [],
            'adoption_rate': []
        }
        self.events = []  # Timeline of significant events
        self.probabilities = {}  # Event likelihoods
        
    def apply_user_intervention(self, intervention, impact_weights):
        # Update simulation based on user input
        self.recalculate_timeline(impact_weights)
        self.trigger_agent_reactions(intervention)