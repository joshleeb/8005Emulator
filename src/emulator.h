#define TRUE 1
#define FALSE 0

typedef struct _emulator {
    int instructionPtr;   // IP
    int instructionStore; // IS
    int register0;        // R0
    int register1;        // R1
} emulator;

emulator newEmulator();
static void displayEmulator(emulator e);
