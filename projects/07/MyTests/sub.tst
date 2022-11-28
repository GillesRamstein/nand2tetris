load sub.asm,
output-file sub.out,
compare-to sub.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2 RAM[257]%D2.6.2;

repeat 30 {
  ticktock;
}
output;
