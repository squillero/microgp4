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

    movl	$-17416, %eax
    movl	$31465, %ebx
    movl	$-406, %ecx
    movl	$30624, %edx

    and %eax, %ecx
    shl $107, %eax
    sub %edx, %eax
    and %edx, %ebx
    jno n14
    shr $33, %ebx
    jz n14
    jne n18
    xor %ecx, %ebx
    cmp %eax, %ecx
    jno n21
n14:
    add %edx, %eax
    jc n22
    jnc n21
    shr $238, %edx
n18:
    jc n19
n19:
    cmp %ebx, %eax
    shl $215, %edx
n21:
    shl $2, %edx
n22:
    sub %ecx, %eax
    jmp n24
n24:
    je n26
    shr $127, %ebx
n26:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
