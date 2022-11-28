load gt.asm,
output-file gt.out,
compare-to gt.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2 RAM[257]%D2.6.2 RAM[258]%D2.6.2 RAM[259]%D2.6.2;

repeat 100 {
  ticktock;
}
output;
