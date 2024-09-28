import pytest 
from Copilot_Bridge_R2 import VectorRenderer, RasterRenderer, Circle  # แก้ไขให้ตรงกับชื่อไฟล์ที่มีคลาสเหล่านี้

def test_vector_renderer():
    # Arrange
    renderer = VectorRenderer()
    radius = 5
    
    # Act
    result = renderer.render_circle(radius)
    
    # Assert
    assert result == "Drawing a circle of radius 5 with VectorRenderer"

def test_raster_renderer():
    # Arrange
    renderer = RasterRenderer()
    radius = 10
    
    # Act
    result = renderer.render_circle(radius)
    
    # Assert
    assert result == "Drawing a circle of radius 10 with RasterRenderer"

def test_circle_with_vector_renderer():
    # Arrange
    renderer = VectorRenderer()
    circle = Circle(renderer, 5)
    
    # Act
    result = circle.draw()
    
    # Assert
    assert result == "Drawing a circle of radius 5 with VectorRenderer"

def test_circle_with_raster_renderer():
    # Arrange
    renderer = RasterRenderer()
    circle = Circle(renderer, 10)
    
    # Act
    result = circle.draw()
    
    # Assert
    assert result == "Drawing a circle of radius 10 with RasterRenderer"
