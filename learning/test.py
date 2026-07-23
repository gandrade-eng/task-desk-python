from PySide6.QtGui import QPixmap

pix = QPixmap(r"C:\Users\Guilh\OneDrive\VS CODE\Projects\task-desk-python\icons\Home.png")

print(pix.isNull())
print(pix.width(), pix.height())