#ifndef SHA256_H
#define SHA256_H

#include <cstddef>
#include <cstdint>

void sha256_hash(const uint8_t *input, size_t length, uint8_t *output);

#endif // SHA256_H
