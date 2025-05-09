import os

# Paths to your directories
duplicate_path = "Duplicate-Report"
success_path = "Successfull-Report"

# Count files in each directory
duplicate_count = len([f for f in os.listdir(duplicate_path) if os.path.isfile(os.path.join(duplicate_path, f))])
success_count = len([f for f in os.listdir(success_path) if os.path.isfile(os.path.join(success_path, f))])
total_count = duplicate_count + success_count

# Generate SVG content
svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="500" height="200" viewBox="0 0 500 200">
  <style>
    .label {{ fill: white; font-family: Arial, sans-serif; font-size: 14px; }}
    .count {{ fill: white; font-family: Arial, sans-serif; font-size: 28px; font-weight: bold; }}
    .circle-label {{ fill: orange; font-family: Arial, sans-serif; font-size: 40px; font-weight: bold; }}
  </style>

  <!-- Background -->
  <rect width="500" height="200" fill="black" rx="10" />

  <!-- Left Section -->
  <text x="60" y="80" class="label" text-anchor="middle">Duplicate</text>
  <text x="60" y="100" class="label" text-anchor="middle">Reports</text>
  <text x="60" y="140" class="count" text-anchor="middle">{duplicate_count}</text>

  <!-- Center Section -->
  <circle cx="250" cy="100" r="40" fill="none" stroke="orange" stroke-width="4" />
  <text x="250" y="108" class="circle-label" text-anchor="middle" dominant-baseline="middle">{total_count}</text>
  <text x="250" y="160" class="label" text-anchor="middle">Total Reports</text>

  <!-- Right Section -->
  <text x="440" y="80" class="label" text-anchor="middle">Successful</text>
  <text x="440" y="100" class="label" text-anchor="middle">Reports</text>
  <text x="440" y="140" class="count" text-anchor="middle">{success_count}</text>
</svg>
'''

# Save to file
with open("report-test.svg", "w") as f:
    f.write(svg_content)

print("✅ SVG generated as report-test.svg")
