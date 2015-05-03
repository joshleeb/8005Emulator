#include <stdio.h>
#include <stdlib.h>
#include "emulator.h"

int main(int argc, char *argv[]) {
    int instructions[512] = {0};
    emulator theEmulator = newEmulator();

    int instruction = getchar();
    for (int i = 0; instruction != EOF && instruction != '\n'; i++) {
        instructions[i] = instruction - '0';
        instruction = getchar();
    }

    for (int i = 0; instructions[i] != '\0'; i++) {
        printf("%d", instructions[i]);
    }

    displayEmulator(theEmulator);

    return EXIT_SUCCESS;
}

emulator newEmulator() {
    emulator new;

    new.instructionPtr = 0;
    new.instructionStore = 0;
    new.register0 = 0;
    new.register1 = 0;

    return new;
}

static void displayEmulator(emulator e) {
    printf("\nIP\tIS\tR0\tR1\n");
    printf("%d\t%d\t%d\t%d\n\n", e.instructionPtr, e.instructionStore,
            e.register0, e.register1);
}
