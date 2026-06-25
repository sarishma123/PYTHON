class Router:
    def send(self, sender, receiver, msg):
        print(f"[Router] {sender} -> {receiver}: {msg}")


router = Router()

router.send("PC1", "PC2", "Hello")