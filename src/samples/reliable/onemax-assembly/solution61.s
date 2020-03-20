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

    movl	$12568, %eax
    movl	$-16823, %ebx
    movl	$-12701, %ecx
    movl	$10745, %edx

    jc n39
    add %eax, %ecx
    shr $82, %ecx
    or %ebx, %edx
    jz n22
    shl $178, %eax
    shl $27, %edx
    shl $120, %edx
    add %ecx, %ebx
    add %ecx, %eax
    shl $74, %ebx
    add %ecx, %edx
    jnz n40
    shl $229, %eax
    jz n18
n18:
    jne n25
    sub %edx, %eax
    and %ebx, %ecx
    shr $24, %ebx
n22:
    jnc n43
    xor %edx, %eax
    jz n40
n25:
    xor %eax, %ebx
    jnz n36
    shl $0, %ecx
    shr $116, %ecx
    shr $119, %eax
    jnc n43
    shl $186, %ebx
    shl $181, %ebx
    xor %eax, %eax
    jne n43
    shr $87, %ebx
n36:
    jnz n43
    jc n43
    jnz n43
n39:
    jnc n43
n40:
    cmp %ebx, %ecx
    shl $142, %eax
    ja n43
n43:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
