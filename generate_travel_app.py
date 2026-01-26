import os
import re

# --- Configuration ---
SOURCE_DIR = r"c:\python-training\travel"
OUTPUT_FILE = os.path.join(SOURCE_DIR, "travel_guide_offline.html")
FILES_TO_PROCESS = [
    "final_itinerary.md",
    "day_01.md",
    "day_02.md",
    "day_03.md",
    "day_04.md",
    "day_05.md",
    "day_06.md",
    "day_07.md",
    "day_08.md",
    "day_09.md",
    "day_10.md",
    "day_11.md",
    "day_12.md",
    "day_13.md",
    "packing_checklist.md",
    "survival_guide.md",
    "phrase_guide.md",
    "asian_food_guide.md",
    # New enhancement guides
    "restaurant_booking_guide.md",
    "emergency_contacts.md",
    "budget_guide.md",
    "photo_timing_guide.md",
    "offline_maps_guide.md",
    "weather_backup_plans.md",
    "luggage_storage_guide.md",
    "transport_booking_guide.md",
    "pre_departure_checklist.md"
]

# --- Color Definitions ---
CITY_COLORS = {
    "final_itinerary": "#2c3e50",       # Dark Blue (General)
    "day_01": "#3498db",                # Bright Blue (Arrival)
    "day_02": "#2ecc71",                # Green (Königssee)
    "day_03": "#1abc9c",                # Turquoise (Lakes)
    "day_04": "#16a085",                # Dark Turquoise (Salzburg)
    "day_05": "#9b59b6",                # Purple (Moving)
    "day_06": "#8e44ad",                # Dark Purple (Innsbruck)
    "day_07": "#e74c3c",                # Red (Budapest)
    "day_08": "#c0392b",                # Dark Red (Castle)
    "day_09": "#e67e22",                # Orange (Thermal)
    "day_10": "#d35400",                # Dark Orange (Vienna)
    "day_11": "#f39c12",                # Yellow (Opera)
    "day_12": "#f1c40f",                # Bright Yellow (Art)
    "day_13": "#95a5a6",                # Grey (Departure)
    "packing_checklist": "#34495e",     # Dark Grey (Checklist)
    "survival_guide": "#e74c3c",        # Red (Emergency)
    "phrase_guide": "#27ae60",          # Green (Language)
    "asian_food_guide": "#d35400"       # Orange (Food)
}

# --- CSS Styles (Embedded for Offline Use) ---
CSS_STYLES = """
<style>
    :root {
        --primary-color: #2c3e50;
        --secondary-color: #3498db;
        --bg-color: #f8f9fa;
        --text-color: #333;
        --card-bg: #fff;
        --header-height: 60px;
    }
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--bg-color);
        margin: 0;
        padding-top: var(--header-height); /* Space for top header */
        padding-bottom: 70px; /* Space for bottom nav */
    }
    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }
    
    /* Sticky Top Header */
    .top-header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: var(--header-height);
        background-color: var(--primary-color);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        z-index: 1001;
        transition: background-color 0.3s ease;
    }
    .header-title {
        font-size: 20px;
        font-weight: bold;
        margin: 0;
    }
    
    /* Navigation */
    .nav-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #fff;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        display: flex;
        justify-content: space-around;
        padding: 10px 0;
        z-index: 1000;
        overflow-x: auto;
    }
    .nav-item {
        color: #666;
        text-decoration: none;
        font-size: 10px;
        text-align: center;
        padding: 6px 6px;
        flex: 0 0 auto; 
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        align-items: center;
        white-space: nowrap;
        background: #f5f5f5;
        border: 1px solid #ddd;
        transition: all 0.2s ease;
        min-width: 50px;
    }
    .nav-item:hover {
        background: #e8e8e8;
        transform: translateY(-2px);
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .nav-item .day-num {
        font-weight: bold;
        font-size: 11px;
        margin-bottom: 2px;
    }
    .nav-item .day-date {
        font-size: 9px;
        color: #888;
    }
    .nav-item .day-city {
        font-size: 8px;
        color: #999;
        margin-top: 1px;
    }
    .nav-item.active {
        color: white;
        font-weight: bold;
        background: var(--primary-color);
        border-color: var(--primary-color);
        box-shadow: 0 3px 8px rgba(0,0,0,0.2);
    }
    .nav-item.active .day-date,
    .nav-item.active .day-city {
        color: rgba(255,255,255,0.9);
    }
    
    /* Content Sections */
    .page-section { display: none; animation: fadeIn 0.3s ease; }
    .page-section.active { display: block; }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    
    /* Elements */
    h1 { display: none; } /* Hide original H1 as we have top header now */
    h2 { color: var(--primary-color); border-bottom: 2px solid #eee; padding-bottom: 5px; margin-top: 30px; }
    h3 { color: #555; border-left: 4px solid var(--primary-color); padding-left: 10px; margin-top: 25px;}
    
    /* Tables */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        background: var(--card-bg);
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        font-size: 14px;
        display: block; /* Horizontal scroll wrapper */
        overflow-x: auto;
    }
    th, td { padding: 12px 8px; text-align: left; border-bottom: 1px solid #eee; min-width: 100px; }
    th { background-color: #f1f1f1; color: #333; font-weight: bold; }
    
    /* Alerts */
    .alert { padding: 15px; border-radius: 8px; margin: 20px 0; border-left: 5px solid; background: #fff; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
    .alert-tip { border-color: #2196f3; }
    .alert-important { border-color: #4caf50; }
    .alert-warning { border-color: #ff9800; }
    
    /* Checklist */
    .checkbox-item {
        background: white;
        padding: 10px;
        border-bottom: 1px solid #eee;
        display: flex;
        align-items: center;
    }
    .checkbox-item label { margin-left: 10px; width: 100%; }
    input[type="checkbox"] { width: 20px; height: 20px; }
</style>
"""

# --- Javascript (Embedded for Interaction) ---
JS_SCRIPTS = """
<script>
    const cityColors = %CITY_COLORS_JSON%;
    const cityNames = %CITY_NAMES_JSON%;

    function showSection(sectionId) {
        // Hide all sections
        document.querySelectorAll('.page-section').forEach(el => el.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
        
        // Show target section
        document.getElementById(sectionId).classList.add('active');
        
        // Highlight nav
        const navLink = document.querySelector(`a[onclick="showSection('${sectionId}')"]`);
        if (navLink) navLink.classList.add('active');
        
        // Update Header Style & Title
        const primaryColor = cityColors[sectionId] || '#2c3e50';
        const header = document.querySelector('.top-header');
        header.style.backgroundColor = primaryColor;
        document.querySelector('.header-title').textContent = cityNames[sectionId];
        
        // Update CSS variable dynamically for headings
        document.documentElement.style.setProperty('--primary-color', primaryColor);
        
        // Scroll to top
        window.scrollTo(0,0);
    }
</script>
"""

# --- Simple Markdown Parser (Custom) ---
def parse_markdown(text):
    html = []
    lines = text.split('\n')
    in_table = False
    in_list = False
    
    for line in lines:
        line = line.strip()
        
        if not line:
            if in_table:
                html.append("</tbody></table>")
                in_table = False
            if in_list:
                html.append("</ul>")
                in_list = False
            continue
            
        # Headers
        if line.startswith('# '):
            pass # Skip H1 as it's used in sticky header now
        elif line.startswith('## '):
            html.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith('### '):
            html.append(f"<h3>{line[4:]}</h3>")
            
        # Alerts
        elif line.startswith('> [!TIP]'):
            html.append('<div class="alert alert-tip"><strong>💡 TIP:</strong>')
        elif line.startswith('> [!IMPORTANT]'):
            html.append('<div class="alert alert-important"><strong>🔔 IMPORTANT:</strong>')
        elif line.startswith('> [!WARNING]') or line.startswith('> [!CAUTION]'):
            html.append('<div class="alert alert-warning"><strong>⚠️ WARNING:</strong>')
        elif line.startswith('> '):
            html.append(f"{line[2:]}<br>")
            if line == lines[-1] or not lines[lines.index(line)+1].startswith('> '):
                 html.append('</div>')

        # Tables
        elif '|' in line and (line.startswith('|') or ' | ' in line):
            cols = [c.strip() for c in line.strip('|').split('|')]
            if '---' in line: continue
            
            if not in_table:
                html.append("<table><thead><tr>")
                for c in cols: html.append(f"<th>{c}</th>")
                html.append("</tr></thead><tbody>")
                in_table = True
            else:
                html.append("<tr>")
                for c in cols: 
                    content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', c)
                    html.append(f"<td>{content}</td>")
                html.append("</tr>")
        
        # Checkboxes
        elif line.startswith('- [ ] ') or line.startswith('- [x] '):
            checked = 'checked' if '[x]' in line else ''
            content = line[6:]
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            html.append(f'<div class="checkbox-item"><input type="checkbox" {checked}><label>{content}</label></div>')
        
        # Lists
        elif line.startswith('- ') or line.startswith('* '):
             if not in_list: html.append("<ul>"); in_list = True
             content = line[2:]
             content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
             html.append(f"<li>{content}</li>")
        
        else:
            line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', line)
            html.append(f"<p>{line}</p>")
            
    return "\n".join(html)

def generate_app():
    nav_items = []
    content_sections = []
    
    name_map = {
        "final_itinerary.md": "總行程表",
        "day_01.md": "Day 1 - 2/17",
        "day_02.md": "Day 2 - 2/18",
        "day_03.md": "Day 3 - 2/19",
        "day_04.md": "Day 4 - 2/20",
        "day_05.md": "Day 5 - 2/21",
        "day_06.md": "Day 6 - 2/22",
        "day_07.md": "Day 7 - 2/23",
        "day_08.md": "Day 8 - 2/24",
        "day_09.md": "Day 9 - 2/25",
        "day_10.md": "Day 10 - 2/26",
        "day_11.md": "Day 11 - 2/27",
        "day_12.md": "Day 12 - 2/28",
        "day_13.md": "Day 13 - 3/1",
        "packing_checklist.md": "行李清單",
        "survival_guide.md": "生存指南",
        "phrase_guide.md": "常用短句",
        "asian_food_guide.md": "亞洲美食"
    }

    # Map Configuration: filename -> map image filename (not used for daily structure)
    map_images = {}
    
    import base64
    import json
    
    # Initialize variables
    first_section = None
    city_colors_json = json.dumps(CITY_COLORS)
    city_names_json = json.dumps({k.replace('.md',''): v for k,v in name_map.items()})

    for filename in FILES_TO_PROCESS:
        filepath = os.path.join(SOURCE_DIR, filename)
        if not os.path.exists(filepath): continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        section_id = filename.replace('.md', '')
        if first_section is None: first_section = section_id
        
        display_name = name_map.get(filename, filename)
        
        # Day metadata: date and location
        day_metadata = {
            "day_01.md": {"date": "2/17", "city": "VIE→SBG"},
            "day_02.md": {"date": "2/18", "city": "國王湖"},
            "day_03.md": {"date": "2/19", "city": "雙湖"},
            "day_04.md": {"date": "2/20", "city": "薩堡"},
            "day_05.md": {"date": "2/21", "city": "→茵堡"},
            "day_06.md": {"date": "2/22", "city": "→維也納"},
            "day_07.md": {"date": "2/23", "city": "→布達"},
            "day_08.md": {"date": "2/24", "city": "城堡山"},
            "day_09.md": {"date": "2/25", "city": "溫泉"},
            "day_10.md": {"date": "2/26", "city": "→維也納"},
            "day_11.md": {"date": "2/27", "city": "美泉宮"},
            "day_12.md": {"date": "2/28", "city": "美景宮"},
            "day_13.md": {"date": "3/1", "city": "離境"}
        }
        
        # Create navigation HTML
        if filename.startswith('day_'):
            day_num = filename.replace('day_', '').replace('.md', '')
            meta = day_metadata.get(filename, {"date": "", "city": ""})
            nav_html = f'''<a href="#" class="nav-item" onclick="showSection('{section_id}')">
                <div class="day-num">D{day_num}</div>
                <div class="day-date">{meta['date']}</div>
                <div class="day-city">{meta['city']}</div>
            </a>'''
        elif display_name == "總行程表":
            nav_html = f'<a href="#" class="nav-item" onclick="showSection(\'{section_id}\')"><div class="day-num">總覽</div></a>'
        elif display_name == "行李清單":
            nav_html = f'<a href="#" class="nav-item" onclick="showSection(\'{section_id}\')"><div class="day-num">行李</div></a>'
        elif display_name == "生存指南":
            nav_html = f'<a href="#" class="nav-item" onclick="showSection(\'{section_id}\')"><div class="day-num">指南</div></a>'
        elif display_name == "常用短句":
            nav_html = f'<a href="#" class="nav-item" onclick="showSection(\'{section_id}\')"><div class="day-num">短句</div></a>'
        elif display_name == "亞洲美食":
            nav_html = f'<a href="#" class="nav-item" onclick="showSection(\'{section_id}\')"><div class="day-num">美食</div></a>'
        else:
            short_name = display_name[:2] if len(display_name)>3 else display_name
            nav_html = f'<a href="#" class="nav-item" onclick="showSection(\'{section_id}\')"><span>{short_name}</span></a>'
        
        nav_items.append(nav_html)
        html_content = parse_markdown(md_content)
        
        # Inject Map if available
        map_html = ""
        if filename in map_images:
            map_path = os.path.join(SOURCE_DIR, map_images[filename])
            # Check if file exists, if not try the artifact path just in case (optional, but stick to local)
            # Actually, we rely on the copy command having run.
            # To be robust, let's look for the map file with a glob if exact match fails? No, keep it simple.
            # If map file exists, read chunks and base64 encode
            
            # Find the actual file (ignoring timestamp suffix if possible? No, users code uses fixed names)
            # Wait, the subagent saved them as map_vienna_TIMESTAMP.png
            # I instructed it to save as map_vienna.png but subagent tool output says:
            # "map_vienna_1769400332540.png"
            # I must handle this dynamic filename or rename the files during copy.
            # I will assume the COPY command used wildcards so the destination has the timestamps too.
            # I need to find the files in the directory that MATCH the pattern.
            
            # Simple approach: Search for file starting with map_vienna in SOURCE_DIR
            candidates = [f for f in os.listdir(SOURCE_DIR) if f.startswith(map_images[filename].replace('.png','')) and f.endswith('.png')]
            if candidates:
                real_map_path = os.path.join(SOURCE_DIR, candidates[0]) # Take the first match
                with open(real_map_path, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                    map_html = f'<div class="map-container"><img src="data:image/png;base64,{encoded_string}" alt="{display_name} Map" style="width:100%; border-radius:8px; margin-bottom:20px; box-shadow:0 2px 5px rgba(0,0,0,0.1);"></div>'

        content_sections.append(f'<div id="{section_id}" class="page-section"><div class="container">{map_html}{html_content}</div></div>')

    # Inject JSON data into JS
    final_js = JS_SCRIPTS.replace('%CITY_COLORS_JSON%', city_colors_json).replace('%CITY_NAMES_JSON%', city_names_json)

    full_html = f"""
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>2026 中歐冬之旅</title>
        {CSS_STYLES}
    </head>
    <body>
        <div class="top-header">
            <div class="header-title">2026 中歐冬之旅</div>
        </div>
        
        <div id="app">
            {''.join(content_sections)}
        </div>
        
        <nav class="nav-bar">
            {''.join(nav_items)}
        </nav>

        {final_js}
        <script>
            // Init
            showSection('{first_section}');
        </script>
    </body>
    </html>
    """
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Generated improved offline app: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_app()
