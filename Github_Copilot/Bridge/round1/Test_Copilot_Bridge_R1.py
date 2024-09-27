# Python

from Copilot_Bridge_R1 import Renderer, VectorRenderer, RasterRenderer, Shape, Circle

# Arrange-Act-Assert (AAA) structure

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
    circle = Circle(renderer, 5)
    
    # Act
    result = circle.draw()
    
    # Assert
    assert result == "Drawing a circle of radius 5 with RasterRenderer"

def test_circle_resize_with_vector_renderer():
    # Arrange
    renderer = VectorRenderer()
    circle = Circle(renderer, 5)
    
    # Act
    circle.resize(2)
    result = circle.draw()
    
    # Assert
    assert result == "Drawing a circle of radius 10 with VectorRenderer"

def test_circle_resize_with_raster_renderer():
    # Arrange
    renderer = RasterRenderer()
    circle = Circle(renderer, 5)
    
    # Act
    circle.resize(2)
    result = circle.draw()
    
    # Assert
    assert result == "Drawing a circle of radius 10 with RasterRenderer"