#include <openssl/sha.h>
#include "sha256.h"

void sha256_hash(const uint8_t *input, size_t length, uint8_t *output) {
    SHA256_CTX ctx;
    SHA256_Init(&ctx);
    SHA256_Update(&ctx, input, length);
    SHA256_Final(output, &ctx);
}
