"""Lab 8.6: Operating Long-Running Agents"""

CHAPTER = "8.6"
print("chapter hook:", CHAPTER)
SLO_HOURS = 24
lease_minutes = 30
elapsed = 12 * 60
renewals = elapsed // lease_minutes
print({"elapsed_min": elapsed, "lease_renewals": renewals, "within_slo": elapsed <= SLO_HOURS * 60})
print("---")
print("change one input above, predict output, re-run")
