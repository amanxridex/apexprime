import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'login.html']

logout_html = """
        <div class="logout-section" style="margin-top: auto;">
            <a href="login.html" onclick="localStorage.removeItem('isLoggedIn');" style="display: flex; align-items: center; gap: 16px; padding: 14px 20px; color: #ef4444; text-decoration: none; border-radius: 14px; font-weight: 500; transition: all 0.2s; background: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239, 68, 68, 0.1);" onmouseover="this.style.background='rgba(239, 68, 68, 0.1)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(239, 68, 68, 0.05)'; this.style.transform='none';">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 20px; height: 20px;"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
                Logout
            </a>
        </div>
"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'class="logout-section"' in content:
        continue

    # Regex to match the end of nav-links ul
    pattern = r'(<li><a href="create-logins\.html".*?</li>\s*</ul>)'
    
    new_content = re.sub(pattern, r'\1' + logout_html, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Added logout section to all sidebars!")
