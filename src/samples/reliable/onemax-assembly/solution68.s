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

    movl	$6579, %eax
    movl	$15477, %ebx
    movl	$-12321, %ecx
    movl	$12258, %edx

    shl $115, %edx
    jne n32
    jnc n12
    add %edx, %ecx
    sub %eax, %edx
    cmp %eax, %edx
    jo n26
    shr $61, %ebx
    jnc n24
n12:
    cmp %eax, %ebx
    jz n25
    sub %ecx, %ebx
    jmp n28
    add %ebx, %edx
    jo n22
    shl $204, %ecx
    jo n30
    xor %edx, %edx
    xor %ecx, %ebx
n22:
    shl $55, %eax
    and %edx, %edx
n24:
    shr $68, %eax
n25:
    shr $27, %eax
n26:
    jo n32
    ja n29
n28:
    or %ecx, %ebx
n29:
    and %eax, %eax
n30:
    jno n32
    or %ebx, %ecx
n32:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
