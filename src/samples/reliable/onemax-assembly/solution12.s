    .file   "solution.c"
    .text
    .globl  _darwin
    .def    _darwin;        .scl    2;      .type   32;     .endef
_darwin:
LFB17:
    .cfi_startproc
    pushl   %ebp
    .cfi_def_cfa_offset 8
    .cfi_offset 5, -8
    movl    %esp, %ebp
    .cfi_def_cfa_register 5

    movl	$-12345, %eax
    movl	$14522, %ebx
    movl	$-11510, %ecx
    movl	$18142, %edx

    xor %eax, %eax
    sub %ebx, %eax
    cmp %eax, %ecx
    or %edx, %edx
    xor %edx, %edx
    jne n15
    xor %eax, %ecx
    or %eax, %ecx
    cmp %edx, %ecx
    shr $112, %edx
    jmp n15
    ja n21
n15:
    shl $108, %ebx
    and %ecx, %ecx
    shr $3, %edx
    shl $89, %ebx
    shl $117, %ecx
    jz n33
n21:
    ja n35
    ja n37
    add %ecx, %edx
    xor %edx, %edx
    shl $58, %edx
    ja n32
    jnz n37
    or %ecx, %eax
    or %eax, %ebx
    jnc n37
    jno n33
n32:
    or %ecx, %ecx
n33:
    sub %ecx, %ebx
    jz n39
n35:
    shr $99, %ecx
    shl $75, %ebx
n37:
    shr $74, %ecx
    shr $88, %ebx
n39:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
