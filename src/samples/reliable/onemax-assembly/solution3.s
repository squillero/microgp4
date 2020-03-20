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

    movl	$-29022, %eax
    movl	$-29482, %ebx
    movl	$5516, %ecx
    movl	$-1522, %edx

    xor %ebx, %eax
    xor %eax, %ebx
    jz n25
    add %ebx, %edx
    jz n26
    je n27
    xor %eax, %eax
    jnc n29
    xor %ecx, %ecx
    sub %ecx, %ebx
    and %edx, %ebx
    cmp %ecx, %edx
    and %eax, %eax
    shl $51, %eax
    shr $135, %ebx
    shl $35, %ebx
    shl $145, %ebx
    shl $154, %eax
    cmp %ecx, %eax
    jnz n27
    jz n24
n24:
    cmp %ebx, %ecx
n25:
    jne n30
n26:
    je n29
n27:
    shr $135, %edx
    shl $26, %eax
n29:
    shl $141, %eax
n30:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
