"""
Badge Generator Service
Generates SVG badges for diagnostic results
"""

from typing import Tuple


class BadgeGenerator:
    """
    Service for generating SVG badges for diagnostic results
    """

    @staticmethod
    def get_category_color(category: str) -> Tuple[str, str]:
        """
        Get colors for category

        Args:
            category: Category name

        Returns:
            Tuple of (hex_color, text_color)
        """
        colors = {
            "Advanced": ("#22c55e", "#ffffff"),  # Green
            "Established": ("#3b82f6", "#ffffff"),  # Blue
            "Emerging": ("#eab308", "#000000"),  # Yellow
            "Foundational": ("#ef4444", "#ffffff"),  # Red
        }
        return colors.get(category, ("#6b7280", "#ffffff"))  # Gray default

    @staticmethod
    def generate_badge_svg(score: int, category: str, size: int = 300) -> str:
        """
        Generate SVG badge for sharing

        Args:
            score: Score 0-100
            category: Category name
            size: Size of badge (default 300x300)

        Returns:
            SVG string
        """
        bg_color, text_color = BadgeGenerator.get_category_color(category)

        # Calculate circle properties
        center = size / 2
        radius = size * 0.35
        circumference = 2 * 3.14159 * radius

        # Calculate stroke dash offset for progress circle
        progress = score / 100
        stroke_offset = circumference * (1 - progress)

        svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="{size}" height="{size}" fill="#ffffff"/>
  
  <!-- Background circle -->
  <circle cx="{center}" cy="{center}" r="{radius}" fill="#f0f0f0"/>
  
  <!-- Progress circle -->
  <circle cx="{center}" cy="{center}" r="{radius}" 
          fill="none" stroke="{bg_color}" stroke-width="{size * 0.03}"
          stroke-dasharray="{circumference}"
          stroke-dashoffset="{stroke_offset}"
          stroke-linecap="round"
          transform="rotate(-90 {center} {center})"/>
  
  <!-- Center circle -->
  <circle cx="{center}" cy="{center}" r="{radius * 0.7}" fill="{bg_color}"/>
  
  <!-- Score text -->
  <text x="{center}" y="{center - size * 0.05}" font-size="{size * 0.35}" 
        font-weight="bold" text-anchor="middle" fill="{text_color}" 
        font-family="Arial, sans-serif">
    {score}
  </text>
  
  <!-- Score label -->
  <text x="{center}" y="{center + size * 0.08}" font-size="{size * 0.08}" 
        text-anchor="middle" fill="{text_color}" font-family="Arial, sans-serif">
    /100
  </text>
  
  <!-- Category -->
  <text x="{center}" y="{center + size * 0.25}" font-size="{size * 0.12}" 
        font-weight="bold" text-anchor="middle" fill="{bg_color}" 
        font-family="Arial, sans-serif">
    {category}
  </text>
  
  <!-- Aivory branding -->
  <text x="{center}" y="{size * 0.92}" font-size="{size * 0.08}" 
        text-anchor="middle" fill="#999999" font-family="Arial, sans-serif">
    Aivory AI Readiness
  </text>
</svg>'''

        return svg.strip()

    @staticmethod
    def generate_card_svg(score: int, category: str, company_name: str = None, width: int = 600, height: int = 400) -> str:
        """
        Generate SVG card for results

        Args:
            score: Score 0-100
            category: Category name
            company_name: Optional company name
            width: Card width
            height: Card height

        Returns:
            SVG string
        """
        bg_color, text_color = BadgeGenerator.get_category_color(category)

        svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="{width}" height="{height}" fill="{bg_color}"/>
  
  <!-- Header -->
  <text x="{width * 0.5}" y="{height * 0.08}" font-size="28" font-weight="bold" 
        text-anchor="middle" fill="{text_color}" font-family="Arial, sans-serif">
    Aivory AI Readiness Assessment
  </text>
  
  <!-- Score section -->
  <text x="{width * 0.5}" y="{height * 0.35}" font-size="80" font-weight="bold" 
        text-anchor="middle" fill="{text_color}" font-family="Arial, sans-serif">
    {score}
  </text>
  
  <text x="{width * 0.5}" y="{height * 0.48}" font-size="32" 
        text-anchor="middle" fill="{text_color}" font-family="Arial, sans-serif">
    {category}
  </text>
  
  <!-- Company name if provided -->
  {f'''<text x="{width * 0.5}" y="{height * 0.62}" font-size="18" 
        text-anchor="middle" fill="{text_color}" font-family="Arial, sans-serif">
    {company_name}
  </text>''' if company_name else ''}
  
  <!-- Footer -->
  <text x="{width * 0.5}" y="{height * 0.92}" font-size="14" 
        text-anchor="middle" fill="{text_color}" opacity="0.8" font-family="Arial, sans-serif">
    Created with Aivory • aivory.ai
  </text>
</svg>'''

        return svg.strip()
