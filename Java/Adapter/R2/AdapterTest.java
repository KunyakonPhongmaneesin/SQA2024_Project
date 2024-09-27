import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class AdapterTest {

    @Test
    public void testRequest() {
        // Arrange
        Adaptee adaptee = new Adaptee();
        Target target = new Adapter(adaptee);

        // Act
        target.request();

        // Assert
        // เนื่องจากเมธอดนี้พิมพ์ข้อความไปที่คอนโซล เราไม่สามารถตรวจสอบผลลัพธ์ได้โดยตรง
        // แต่เราสามารถตรวจสอบว่าไม่มีข้อยกเว้นเกิดขึ้น
        assertDoesNotThrow(() -> target.request());
    }
}